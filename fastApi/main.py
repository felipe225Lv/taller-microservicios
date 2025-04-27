from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastApi.api.v1 import Animal_routes, Cage_routes
import os

# FastAPI app
app = FastAPI(
    title="FastAPI Example",
    root_path="",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
    },
)

app.include_router(Animal_routes.router, prefix="/api/v1/animal")
app.include_router(Cage_routes.router, prefix="/api/v1/cage")

