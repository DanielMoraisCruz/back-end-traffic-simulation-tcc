import random

import pytest
from fastapi.testclient import TestClient

import app
from sqlalchemy import create_engine
from SqlAlchemy.models import table_registry
from sqlalchemy.orm import Session


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def population():
    return [
        [
            {'redDuration': 10, 'greenDuration': 10, 'cycleStartTime': 10},
            {'redDuration': 20, 'greenDuration': 20, 'cycleStartTime': 20},
            {'redDuration': 30, 'greenDuration': 30, 'cycleStartTime': 30},
        ],
        [
            {'redDuration': 15, 'greenDuration': 15, 'cycleStartTime': 15},
            {'redDuration': 25, 'greenDuration': 25, 'cycleStartTime': 25},
            {'redDuration': 35, 'greenDuration': 35, 'cycleStartTime': 35},
        ],
    ]


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
