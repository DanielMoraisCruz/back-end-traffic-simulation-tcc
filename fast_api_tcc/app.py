from fastapi import Depends, FastAPI, HTTPException

from schemas import (
    All,
    BaseSimulation,
    Done,
    FinalResults,
    ProcessResults,
    ReturnBaseSimulation,
    ReturnProcessResults,
)
from SqlAlchemy.database import (
    get_config_algGen,
    get_session,
    new_simulation_iteration,
    save_config_algGen,
)
from SqlAlchemy.models import RoadCrossing, SimulationIteration
from sqlalchemy.orm import Session

app = FastAPI()


@app.post('/simulation/create', response_model=ReturnBaseSimulation)
def create_simulation(simulation: BaseSimulation, session: Session = Depends(get_session)):
    try:
        config = save_config_algGen(
            session,
            config_algGen={
                'population': simulation.population,
                'selecteds': simulation.selecteds,
                'mutation_rate': simulation.mutationRate,
            },
        )
        return {'ID': config.configId}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao criar simulação: {e}')


@app.post('/simulation/process-results/{id}', response_model=ReturnProcessResults)
def process_results(id: int, results: ProcessResults, session: Session = Depends(get_session)):
    try:
        simulation_iteration = new_simulation_iteration(
            session,
            SimulationIteration(
                duration=results.simulatedTime,
                tripAvg=results.avgTime,
                tripPeak=results.carsTotal,
                densityPeak=results.occupationRate,
                densityAvg=results.avgSpeed,
                vehiclesTotal=results.carsTotal,
                trafficLights=[
                    RoadCrossing(
                        simulation_id=id,
                        redDuration=light['redDuration'],
                        greenDuration=light['greenDuration'],
                        cycleStartTime=light['cycleStartTime'],
                    )
                    for light in results.lights
                ],
            ),
        )
        return {'lights': [light.simulation_id for light in simulation_iteration.trafficLights]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao processar resultados: {e}')


@app.post('/simulation/done/{id}', response_model=Done)
def check_simulation_done(id: int, session: Session = Depends(get_session)):
    try:
        # Aqui você deve implementar a lógica para verificar se a simulação acabou
        # Exemplo fictício de verificação:
        config = get_config_algGen(session)
        done = config is None or config.population == 0  # exemplo simples
        return {'done': done}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao verificar simulação: {e}')


@app.post('/simulation/premature-termination/{id}')
def premature_termination(id: int, session: Session = Depends(get_session)):
    try:
        # Implementar lógica de término prematuro
        # Por exemplo, remover a simulação do banco de dados
        session.query(SimulationIteration).filter_by(simulationId=id).delete()
        session.commit()
        return {'status': 'success'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao terminar simulação: {e}')


@app.get('/simulation/final-results/{id}', response_model=FinalResults)
def get_final_results(id: int, session: Session = Depends(get_session)):
    try:
        # Lógica para buscar resultados finais
        results = session.query(SimulationIteration).filter_by(simulationId=id).first()
        if results:
            return results  # Deverá adaptar ao modelo de FinalResults
        else:
            raise HTTPException(status_code=404, detail='Resultados não encontrados')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao buscar resultados: {e}')


@app.get('/simulation/all', response_model=All)
def get_all_simulations(session: Session = Depends(get_session)):
    try:
        simulations = session.query(SimulationIteration).all()
        return simulations  # Deverá adaptar ao modelo de All
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao buscar todas simulações: {e}')
