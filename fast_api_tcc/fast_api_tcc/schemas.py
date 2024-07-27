from pydantic import BaseModel


class RoadCrossing(BaseModel):
    roadCrossingId: int
    simulationId: int
    redDuration: int
    greenDuration: int
    cycleStartTime: int


class PostRoadCrossing(BaseModel):
    simulation_id: int
    redDuration: int
    greenDuration: int
    cycleStartTime: int


class SimulationIteration(BaseModel):
    simulationId: int
    duration: int
    tripAvg: int
    tripPeak: int
    densityPeak: int
    densityAvg: int
    vehiclesTotal: int
    roadCrossings: list[PostRoadCrossing]


class PostSimulationIteration(BaseModel):
    duration: int
    tripAvg: int
    tripPeak: int
    densityPeak: int
    densityAvg: int
    vehiclesTotal: int
    roadCrossings: list[PostRoadCrossing]
