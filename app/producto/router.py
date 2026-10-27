
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session

from app.core.database import engine
from app.producto.schema import (
    ProductoCreate,
    ProductoRead,
    ProductoUpdate,
    ProductoCategoriaCreate,
)
from app.producto import service


router = APIRouter(prefix="/productos", tags=["Productos"])


def obtener_sesion():
    with Session(engine) as session:
        yield session


@router.get("/", response_model=list[ProductoRead])
def listar_productos(session: Session = Depends(obtener_sesion)):
    return service.listar_productos(session)


@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(
    producto_id: int,
    session: Session = Depends(obtener_sesion),
):
    producto = service.obtener_producto(session, producto_id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return producto


@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def crear_producto(
    datos: ProductoCreate,
    session: Session = Depends(obtener_sesion),
):
    return service.crear_producto(session, datos)


@router.put("/{producto_id}", response_model=ProductoRead)
def actualizar_producto(
    producto_id: int,
    datos: ProductoUpdate,
    session: Session = Depends(obtener_sesion),
):
    producto = service.obtener_producto(session, producto_id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return service.actualizar_producto(session, producto, datos)


@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(
    producto_id: int,
    session: Session = Depends(obtener_sesion),
):
    producto = service.obtener_producto(session, producto_id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    service.eliminar_producto(session, producto)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/{producto_id}/categorias",
    status_code=status.HTTP_201_CREATED,
)
def asociar_categoria(
    producto_id: int,
    datos: ProductoCategoriaCreate,
    session: Session = Depends(obtener_sesion),
):
    producto = service.obtener_producto(session, producto_id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    asociacion = service.asociar_categoria(
        session,
        producto_id,
        datos.categoria_id,
    )

    if asociacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        )

    return {
        "producto_id": asociacion.producto_id,
        "categoria_id": asociacion.categoria_id,
    }


@router.get("/{producto_id}/categorias")
def listar_categorias_producto(
    producto_id: int,
    session: Session = Depends(obtener_sesion),
):
    categorias = service.listar_categorias_producto(session, producto_id)

    if categorias is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    return categorias


@router.delete(
    "/{producto_id}/categorias/{categoria_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def desasociar_categoria(
    producto_id: int,
    categoria_id: int,
    session: Session = Depends(obtener_sesion),
):
    producto = service.obtener_producto(session, producto_id)

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado",
        )

    eliminada = service.desasociar_categoria(
        session,
        producto_id,
        categoria_id,
    )

    if not eliminada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Asociación no encontrada",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
