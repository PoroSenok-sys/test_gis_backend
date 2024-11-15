"""Модели для базы данных (ORM)"""
from datetime import datetime
from typing import Annotated

from sqlalchemy import Integer, Float, String, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTable

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


class User(SQLAlchemyBaseUserTable[int], Base):
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String, nullable=False
    )
    registered_at: Mapped[str] = mapped_column(
        TIMESTAMP, default=datetime.now())
