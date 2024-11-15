"""Модели для базы данных (ORM)"""
from typing import Annotated

from sqlalchemy import Integer, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base

type_intpk = Annotated[int, mapped_column(primary_key=True)]


class Circle(Base):
    """
    Модель для получения данных от пользователя\n
    Атрибуты:\n
    latitude - Широта в EPSG:4326\n
    longitude - Долгота в EPSG:4326\n
    radius - Радиус в метрах
    """
    __tablename__ = "circle_cache"

    id: Mapped[type_intpk]
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    radius: Mapped[float] = mapped_column(Float, nullable=False)
    num_points: Mapped[int] = mapped_column(Integer, default=100)

    geojson: Mapped[JSONB] = mapped_column(JSONB, nullable=False)
