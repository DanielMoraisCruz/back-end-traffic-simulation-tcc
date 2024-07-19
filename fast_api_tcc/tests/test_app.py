from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_tcc.app import app

from fast_api_tcc.schemas import SimulationIteration, TrafficLight, PostTrafficLight

from fast_api_tcc.tests.conftest import client

def test_simulation(client: TestClient):
    simulation_iteration = SimulationIteration(
        id=1,
        duration=1,
        tripAvg=1,
        tripPeak=1,
        densityPeak=1,
        densityAvg=1,
        vehiclesTotal=1,
        trafficLights=[
            TrafficLight(
                id=1,
                redDuration=1,
                greenDuration=1,
                cycleStartTime=1,
                cycleStartTimeOffset=1
            )
        ]
    )
    response = client.post('/simulation/', json=simulation_iteration.dict())
    assert response.status_code == HTTPStatus.OK
    assert response.json() == simulation_iteration.dict()


def test_traffic_light(client: TestClient):
    traffic_light = PostTrafficLight(
        redDuration=1,
        greenDuration=1,
        cycleStartTime=1,
        cycleStartTimeOffset=1
    )
    response = client.post('/traffic_light/', json=traffic_light.dict())
    assert response.status_code == HTTPStatus.OK
    assert response.json() == traffic_light.dict()

