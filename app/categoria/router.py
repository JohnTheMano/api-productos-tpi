
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session

from app.core.database import get_session
from app.categoria import service
from app.categoria.schema import CategoriaCreate, CategoriaRead, CategoriaUpdate


router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"],
)


@router.get("/", response_model=list[CategoriaRead])
def listar_categorias(
    session: Session = Depends(get_session),
):
    return service.listar_categorias(session)


@router.get("/{categoria_id}", response_model=CategoriaRead)
def obtener_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
):
    categoria = service.obtener_categoria(session, categoria_id)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )

    return categoria


@router.post(
    "/",
    response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED,
)
def crear_categoria(
    datos: CategoriaCreate,
    session: Session = Depends(get_session),
):
    return service.crear_categoria(session, datos)


@router.put("/{categoria_id}", response_model=CategoriaRead)
def actualizar_categoria(
    categoria_id: int,
    datos: CategoriaUpdate,
    session: Session = Depends(get_session),
):
    categoria = service.obtener_categoria(session, categoria_id)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )

    return service.actualizar_categoria(session, categoria, datos)


@router.delete(
    "/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
):
    categoria = service.obtener_categoria(session, categoria_id)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )

    service.eliminar_categoria(session, categoria)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
