from pydantic import BaseModel


class TrafficLight(BaseModel):
    id: int
    redDuration: int
    greenDuration: int
    cycleStartTime: int


class PostTrafficLight(BaseModel):
    redDuration: int
    greenDuration: int
    cycleStartTime: int


class SimulationIteration(BaseModel):
    id: int
    duration: int
    tripAvg: int
    tripPeak: int
    densityPeak: int
    densityAvg: int
    vehiclesTotal: int
    trafficLights: list[TrafficLight]
