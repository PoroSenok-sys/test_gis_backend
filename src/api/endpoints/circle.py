"""Эндпоинт для выполнения операции расчета круга"""
from asyncio import sleep

import geopandas as gpd
import json

from fastapi import APIRouter

from src.api.models.circle import CircleRequest
from src.db.crud import create_cache_circle_data, get_cache_circle_data
from src.services.circle_service import create_circle

router = APIRouter(
    prefix="/circle",
    tags=["Coverage calculation"]
)


@router.post("/generate-circle")
async def generate_circle(request: CircleRequest):
    """
    Эндпоинт для генерации круга в GeoJSON-формате
    по координатам и радиусу.
    """
    data_in_cache = await get_cache_circle_data(latitude=request.latitude, longitude=request.longitude,
                                                radius=request.radius, num_points=request.num_points)
    if data_in_cache:
        return data_in_cache[0]["Circle"].geojson
    # Генерация полигона круга
    circle = create_circle(request.longitude, request.latitude, request.radius)

    # Преобразуем в GeoJSON
    geojson = gpd.GeoSeries([circle]).to_json()

    await create_cache_circle_data(longitude=request.longitude,
                                   latitude=request.latitude,
                                   radius=request.radius,
                                   geojson=json.loads(geojson))

    # Имитируем длительную операцию и возвращаем GeoJSON
    await sleep(5)
    return json.loads(geojson)

