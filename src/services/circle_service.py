"""Логика работы с гео-данными (например, создание кругов)"""
from math import radians, cos, sin
from shapely.geometry.polygon import Polygon


# Функция для вычисления координат точек круга
def create_circle(lon: float, lat: float, radius: float, num_points: int = 100):
    """Генерируем круг, используя радиус и координаты центра (lon, lat)."""
    # Переводим радиус в градусы
    radius_deg = radius / 111320  # 1 градус ~ 111.32 км
    angle_step = 360 / num_points  # Угол между точками круга

    # Список точек круга
    circle_points = []
    for i in range(num_points):
        angle = radians(i * angle_step)
        dlat = radius_deg * cos(angle)
        dlon = radius_deg * sin(angle)

        # Новая точка
        new_lat = lat + dlat
        new_lon = lon + dlon
        circle_points.append((new_lon, new_lat))

    # Замкнем круг
    circle_points.append(circle_points[0])

    return Polygon(circle_points)
