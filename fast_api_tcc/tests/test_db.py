from sqlalchemy import select

from fast_api_tcc.SqlAlchemy.models import TrafficLight


def test_create_traffic_light_table(session):
    traffic_light = TrafficLight(
        redDuration=10,
        greenDuration=10,
        cycleStartTime=10,
    )
    session.add(traffic_light)
    session.commit()
    session.scalar(select(TrafficLight).where(TrafficLight.id == 1))

    assert traffic_light.id == 1
