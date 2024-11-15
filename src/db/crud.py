"""Логика работы с базой данных"""
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from src.core.database import async_session_factory
from src.db.models import Circle


async def create_cache_circle_data(latitude: float, longitude: float, radius: float,
                                   geojson: dict, num_points: int = 100):
    """Функция по созданию объекта модели Circle и занесению её в БД"""
    async with async_session_factory() as session:
        new_cache = insert(Circle).values(
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            num_points=num_points,
            geojson=geojson
        )

        # Добавляем в сессию и сохраняем в базе данных
        await session.execute(new_cache)
        await session.commit()

        return {"status": "success"}


async def get_cache_circle_data(latitude: float, longitude: float, radius: float, num_points: int = 100):
    """Функция для получения объекта модели Circle из БД"""
    async with async_session_factory() as session:
        circle = select(Circle).filter(
            Circle.latitude == latitude,
            Circle.longitude == longitude,
            Circle.radius == radius,
            Circle.num_points == num_points,
        )
        result = await session.execute(circle)

        return result.mappings().all()

