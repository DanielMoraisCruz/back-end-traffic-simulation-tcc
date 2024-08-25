from pydantic import BaseModel


class BaseSimulation(BaseModel):
    """
    POST /simulation/create [Cria simulação]
        Back recebe objeto com population, simulatedTime,
        mutationRate, selecteds
        Front recebe ID
    """

    population: list
    simulatedTime: int
    mutationRate: float
    selecteds: int


class ReturnBaseSimulation(BaseModel):
    ID: int


class ProcessResults(BaseModel):
    """
    POST /simulation/process-results/{id} [processa resultados da geração]
        Back recebe array de avgTime, carsTotal, simulatedTime, avgSpeed,
        occupationRate, lights[], iterateNext
        Front recebe lights[]
    """

    avgTime: int
    carsTotal: int
    simulatedTime: int
    avgSpeed: int
    occupationRate: int
    lights: list
    iterateNext: bool


class ReturnProcessResults(BaseModel):
    # lights[]
    lights: list


class Done(BaseModel):
    """
    POST /simulation/done/{id} [retorna se simulação acabou ou não]
        Front recebe array com 1 item true ou false
    """

    done: bool


class PrematureTermination(BaseModel):
    """
    POST /simulation/premature-termination/{id}
        Retorna status 200 se der certo
        qualquer erro retornar erro 5XX
    """

    pass


class FinalResults(BaseModel):
    """
    GET /simulation/final-results/{id} [retorna estatíticas]
        Front recebe resultados
    """

    pass


class All(BaseModel):
    """
    GET /simulation/all
        Retorna lista de todas otimizações feitas
    """

    pass
