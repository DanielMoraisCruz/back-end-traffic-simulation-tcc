import random

import pytest
from fastapi.testclient import TestClient

from schemas import BaseSimulation, ProcessResults
from sqlalchemy.orm import Session

# Definindo constantes para os códigos de status HTTP
HTTP_STATUS_OK = 200
HTTP_STATUS_NOT_FOUND = 404


@pytest.fixture
def random_population():
    def generate_traffic_light():
        return {
            'redDuration': random.randint(1, 60),
            'greenDuration': random.randint(1, 60),
            'cycleStartTime': random.randint(1, 120),
        }

    def generate_population(size=2):
        return [[generate_traffic_light() for _ in range(3)] for _ in range(size)]

    return generate_population


def test_create_simulation(client: TestClient, session: Session, population):
    simulation_data = BaseSimulation(
        population=population, simulatedTime=1000, mutationRate=0.05, selecteds=2
    )

    response = client.post('/simulation/create', json=simulation_data.dict())
    assert response.status_code == HTTP_STATUS_OK
    assert 'ID' in response.json()


def test_process_results(client: TestClient, session: Session, random_population):
    population = random_population()
    simulation_data = BaseSimulation(
        population=population, simulatedTime=1000, mutationRate=0.05, selecteds=2
    )

    create_response = client.post('/simulation/create', json=simulation_data.dict())
    assert create_response.status_code == HTTP_STATUS_OK
    simulation_id = create_response.json()['ID']

    results_data = ProcessResults(
        avgTime=50,
        carsTotal=100,
        simulatedTime=1000,
        avgSpeed=40,
        occupationRate=80,
        lights=population[0],
        iterateNext=True,
    )

    response = client.post(f'/simulation/process-results/{simulation_id}', json=results_data.dict())
    assert response.status_code == HTTP_STATUS_OK
    assert 'lights' in response.json()


def test_check_done(client: TestClient, session: Session):
    response = client.post('/simulation/done/1')
    assert response.status_code == HTTP_STATUS_OK
    assert 'done' in response.json()
    assert isinstance(response.json()['done'], bool)


def test_premature_termination(client: TestClient, session: Session):
    response = client.post('/simulation/premature-termination/1')
    assert response.status_code == HTTP_STATUS_OK


def test_final_results(client: TestClient, session: Session):
    response = client.get('/simulation/final-results/1')
    assert response.status_code in {HTTP_STATUS_OK, HTTP_STATUS_NOT_FOUND}


def test_get_all_simulations(client: TestClient, session: Session):
    response = client.get('/simulation/all')
    assert response.status_code == HTTP_STATUS_OK
    assert isinstance(response.json(), list)
