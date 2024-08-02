from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy.sql import func

table_registry = registry()


@table_registry.mapped_as_dataclass
class SimulationIteration:
    __tablename__ = 'Simulation_Iteration'

    simulationId: Mapped[int] = mapped_column(init=False, primary_key=True)
    duration: Mapped[int] = mapped_column()
    tripAvg: Mapped[int] = mapped_column()
    tripPeak: Mapped[int] = mapped_column()
    densityPeak: Mapped[int] = mapped_column()
    densityAvg: Mapped[int] = mapped_column()
    vehiclesTotal: Mapped[int] = mapped_column()
    trafficLights: Mapped[list] = mapped_column(
        init=False, relationship='RoadCrossing', back_populates='simulationId'
    )
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )


@table_registry.mapped_as_dataclass
class RoadCrossing:
    __tablename__ = 'Traffic_Light'

    roadCrossingtId: Mapped[int] = mapped_column(init=False, primary_key=True)
    simulation_id: Mapped[int] = mapped_column(foreign_key='SimulationIteration.simulationId')
    redDuration: Mapped[int] = mapped_column()
    greenDuration: Mapped[int] = mapped_column()
    cycleStartTime: Mapped[int] = mapped_column()
    creater_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
