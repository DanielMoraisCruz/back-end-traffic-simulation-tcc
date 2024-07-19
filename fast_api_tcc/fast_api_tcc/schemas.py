from pydantic import BaseModel


class TrafficLight(BaseModel):
    id: int # autoincrement
    redDuration: int
    greenDuration: int
    cycleStartTime: int
    cycleStartTimeOffset: int

class PostTrafficLight(BaseModel):
    redDuration: int
    greenDuration: int
    cycleStartTime: int
    cycleStartTimeOffset: int

class SimulationIteration(BaseModel):
    id: int
    duration: int
    tripAvg: int
    tripPeak: int
    densityPeak: int
    densityAvg: int
    vehiclesTotal: int
    trafficLights: list[TrafficLight]
