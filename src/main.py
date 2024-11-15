"""Точка входа в приложение FastAPI"""
import os
import sys

from fastapi import FastAPI

from src.api.endpoints.circle import router as router_geo_data
from src.api.models.user import UserRead, UserCreate
from src.core.security import fastapi_users, auth_backend

sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = FastAPI(
    title="Coverage calculation"
)

app.include_router(router_geo_data)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
