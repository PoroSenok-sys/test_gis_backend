"""Точка входа в приложение FastAPI"""
import os
import sys

from fastapi import FastAPI

from src.api.endpoints.circle import router as router_geo_data

sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = FastAPI(
    title="Coverage calculation"
)

app.include_router(router_geo_data)
