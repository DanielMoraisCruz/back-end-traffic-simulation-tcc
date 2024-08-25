from settings import Settings
from SqlAlchemy import loggings
from sqlalchemy import create_engine
from SqlAlchemy.models import ConfigAlgGen, RoadCrossing, SimulationIteration
from sqlalchemy.orm import Session

engine = create_engine(Settings().DATABASE_URL)
log = loggings.Log('database')


def get_session() -> Session:
    with Session(engine) as session:
        # yield session
        return session


def new_road_crossing(session, road_crossing: RoadCrossing):
    try:
        session.add(
            RoadCrossing(
                simulation_id=road_crossing.simulation_id,
                redDuration=road_crossing.redDuration,
                greenDuration=road_crossing.greenDuration,
                cycleStartTime=road_crossing.cycleStartTime,
            )
        )
    except Exception as e:
        log.log_error(f'Erro ao criar o cruzament o: {e}')


def new_simulation_iteration(session, simulation_iteration: SimulationIteration):
    try:
        simulation = SimulationIteration(
            duration=simulation_iteration.duration,
            tripAvg=simulation_iteration.tripAvg,
            tripPeak=simulation_iteration.tripPeak,
            densityPeak=simulation_iteration.densityPeak,
            densityAvg=simulation_iteration.densityAvg,
            vehiclesTotal=simulation_iteration.vehiclesTotal,
        )
        session.add(simulation)
        for road_crossing in simulation_iteration.roadCrossings:
            new_road_crossing(session, road_crossing)

        session.commit()
        return simulation_iteration
    except Exception as e:
        log.log_error(f'Error creating simulation: {e}')


# Salvar config algGen no banco de dados
def save_config_algGen(session, config_algGen: ConfigAlgGen):
    try:
        session.add(
            ConfigAlgGen(
                population=config_algGen.population,
                num_selecteds=config_algGen.selecteds,
                mutation_rate=config_algGen.mutation_rate,
            )
        )
        session.commit()
    except Exception as e:
        log.log_error(f'Error config AlgGen: {e}')


# Pegar config algGen do banco de dados
def get_config_algGen(session) -> ConfigAlgGen:
    try:
        return session.query(ConfigAlgGen).first()
    except Exception as e:
        log.log_error(f'Error config AlgGen: {e}')
        return None


# Atualizar config algGen no banco de dados
def patch_config_algGen(
    session, new_population: list, num_selecteds: int = 2, mutation_rate: float = 0.1
) -> ConfigAlgGen:
    try:
        config = session.query(ConfigAlgGen).first()
        config.population = new_population
        config.selecteds = num_selecteds
        config.mutation_rate = mutation_rate
        session.commit()
        return config
    except Exception as e:
        log.log_error(f'Error config AlgGen: {e}')
        return None
