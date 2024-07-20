from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy.sql import func

table_registry = registry()


@table_registry.mapped_as_dataclass
class TrafficLight:
    __tablename__ = 'Traffic_Light'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    redDuration: Mapped[int] = mapped_column()
    greenDuration: Mapped[int] = mapped_column()
    cycleStartTime: Mapped[int] = mapped_column()
    cycleStartTimeOffset: Mapped[int] = mapped_column()
    creater_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
