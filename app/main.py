from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app.core.database import engine
from app.categoria.router import router as categoria_router
from app.categoria import model as categoria_model
from app.producto.router import router as producto_router
from app.producto import model as producto_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="API de Productos",
    description="API para gestionar categorías y productos",
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(categoria_router)
app.include_router(producto_router)

@app.get("/")
def inicio():
    return {"mensaje": "API de Productos funcionando"}
