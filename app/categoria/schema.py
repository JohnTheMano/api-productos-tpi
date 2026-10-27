
from sqlmodel import SQLModel, Field


class CategoriaBase(SQLModel):
    nombre: str = Field(
        max_length=100,
    )
    descripcion: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(SQLModel):
    nombre: str | None = Field(
        default=None,
        max_length=100,
    )
    descripcion: str | None = None


class CategoriaRead(CategoriaBase):
    id: int
