from fastapi import FastAPI

from fast_api_tcc.schemas import SimulationIteration, TrafficLight, PostTrafficLight

app = FastAPI()


@app.post('/simulation/')
async def simulation(simulation_iteration_: SimulationIteration):
    return simulation_iteration_


@app.post('/traffic_light/', response_model=TrafficLight)
async def traffic_light(traffic_light_: PostTrafficLight):
    return traffic_light_

