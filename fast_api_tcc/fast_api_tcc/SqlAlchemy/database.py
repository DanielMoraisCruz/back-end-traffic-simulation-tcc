from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_api_tcc.settings import Settings
from fast_api_tcc.SqlAlchemy.models import RoadCrossing, SimulationIteration

engine = create_engine(Settings().DATABASE_URL)


def get_session() -> Session:
    with Session(engine) as session:
        # yield session
        return session


def new_road_crossing(session, road_crossing: RoadCrossing):
    session.add(
        RoadCrossing(
            simulation_id=road_crossing.simulation_id,
            redDuration=road_crossing.redDuration,
            greenDuration=road_crossing.greenDuration,
            cycleStartTime=road_crossing.cycleStartTime,
        )
    )


def new_simulation_iteration(session, simulation_iteration):
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
