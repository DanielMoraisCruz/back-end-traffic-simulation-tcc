from fastapi import FastAPI
from Logs.loggings import Log
from SqlAlchemy.database import (
    get_session,
    new_road_crossing,
    new_simulation_iteration,
)

from fast_api_tcc.schemas import (
    PostRoadCrossing,
    PostSimulationIteration,
    RoadCrossing,
    SimulationIteration,
)

app = FastAPI()
log = Log('app')


@app.post('/simulation/', response_model=SimulationIteration)
async def crate_simulation(SimulationIteration: PostSimulationIteration):
    log.log_info('Creating simulation')
    session = get_session()
    return new_simulation_iteration(session, SimulationIteration)


@app.post('/road_crossing/', response_model=RoadCrossing)
async def road_crossing(roadCrossing: PostRoadCrossing):
    log.log_info('Creating road crossing')
    session = get_session()
    return new_road_crossing(session, roadCrossing)
