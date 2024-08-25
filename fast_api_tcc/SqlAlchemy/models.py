from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship
from sqlalchemy.sql import func

table_registry = registry()


@table_registry.mapped_as_dataclass
class SimulationIteration:
    __tablename__ = 'Simulation_Iteration'

    simulationId: Mapped[int] = mapped_column(init=False, primary_key=True)
    duration: Mapped[int] = mapped_column(nullable=False)
    tripAvg: Mapped[int] = mapped_column(nullable=False)
    tripPeak: Mapped[int] = mapped_column(nullable=False)
    densityPeak: Mapped[int] = mapped_column(nullable=False)
    densityAvg: Mapped[int] = mapped_column(nullable=False)
    vehiclesTotal: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )

    # Definindo o relacionamento corretamente
    trafficLights: Mapped[list['RoadCrossing']] = relationship(
        'RoadCrossing', back_populates='simulation'
    )


@table_registry.mapped_as_dataclass
class RoadCrossing:
    __tablename__ = 'Traffic_Light'

    roadCrossingId: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    simulation_id: Mapped[int] = mapped_column(
        ForeignKey('Simulation_Iteration.simulationId'), nullable=False
    )
    redDuration: Mapped[int] = mapped_column(nullable=False)
    greenDuration: Mapped[int] = mapped_column(nullable=False)
    cycleStartTime: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    # Definição do relacionamento com SimulationIteration
    simulation: Mapped['SimulationIteration'] = relationship(
        'SimulationIteration', back_populates='trafficLights'
    )


@table_registry.mapped_as_dataclass
class ConfigAlgGen:
    __tablename__ = 'Config_AlgGen'

    configId: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    population: Mapped[int] = mapped_column(nullable=False)
    num_selecteds: Mapped[int] = mapped_column(nullable=False)
    mutation_rate: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
