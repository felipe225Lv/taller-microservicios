from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from api.v1.Animal_routes import router as animal_router
from api.v1.Cage_routes import router as cage_router
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

app.include_router(animal_router, prefix="/api/v1/animal")
app.include_router(cage_router, prefix="/api/v1/cage")

