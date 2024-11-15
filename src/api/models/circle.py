"""Pydantic модель Circle для валидации данных"""
from typing import Optional

from pydantic import BaseModel, Field, field_validator, model_validator


class CircleRequest(BaseModel):
    """
    Модель для получения данных от пользователя\n
    Атрибуты модели:\n
    latitude - Широта в EPSG:4326\n
    longitude - Долгота в EPSG:4326\n
    radius - Радиус в метрах
    """
    # Широта должна быть в пределах -90 до 90 градусов
    latitude: float = Field(..., ge=-90, le=90, description="Широта точки в градусах (от -90 до 90)")

    # Долгота должна быть в пределах -180 до 180 градусов
    longitude: float = Field(..., ge=-180, le=180, description="Долгота точки в градусах (от -180 до 180)")

    # Радиус должен быть положительным числом, выраженным в метрах
    radius: float = Field(gt=0, ge=1, description="Радиус круга в метрах (больше 0)")

    # Дополнительное поле для опциональных настроек, например, для количества точек круга
    num_points: Optional[int] = Field(100, ge=3, le=1000, description="Количество точек на круге (от 3 до 1000)")

    @classmethod
    @field_validator('radius')
    def check_radius_type(cls, v):
        if not isinstance(v, (int, float)):
            raise ValueError(f'Радиус должен быть числом (целым или с плавающей запятой), но получено {type(v).__name__}.')
        if v <= 0:
            raise ValueError('Радиус должен быть положительным числом больше 0.')
        return v

    @classmethod
    @field_validator('latitude', 'longitude')
    def check_coordinates_type(cls, v, field):
        if not isinstance(v, (int, float)):
            raise ValueError(f'{field.name.capitalize()} должно быть числом (целым или с плавающей запятой), '
                             f'но получено {type(v).__name__}.')
        if field.name == 'latitude' and not (-90 <= v <= 90):
            raise ValueError('Широта должна быть в пределах от -90 до 90 градусов.')
        if field.name == 'longitude' and not (-180 <= v <= 180):
            raise ValueError('Долгота должна быть в пределах от -180 до 180 градусов.')
        return v

    @classmethod
    @model_validator(mode='before')
    def validate_data(cls, values):
        """
        Данный валидатор сработает до применения других валидаторов (mode='before').
        Он позволяет контролировать ошибку JSON, если поля имеют неверный тип.
        """
        for field_name, value in values.items():
            # Если значение поля уже некорректное, выбрасываем ошибку
            if not isinstance(value, (int, float)) and field_name in ['latitude', 'longitude', 'radius']:
                raise ValueError(f'{field_name.capitalize()} должно быть числом (целым или с плавающей запятой).')
        return values
