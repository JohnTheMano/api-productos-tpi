
from sqlmodel import Session, select

from app.producto.model import Producto, ProductoCategoria
from app.producto.schema import ProductoCreate, ProductoUpdate
from app.categoria.model import Categoria


def listar_productos(session: Session) -> list[Producto]:
    return session.exec(select(Producto)).all()


def obtener_producto(session: Session, producto_id: int) -> Producto | None:
    return session.get(Producto, producto_id)


def crear_producto(session: Session, datos: ProductoCreate) -> Producto:
    producto = Producto.model_validate(datos)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def actualizar_producto(
    session: Session,
    producto: Producto,
    datos: ProductoUpdate,
) -> Producto:
    cambios = datos.model_dump(exclude_unset=True)
    producto.sqlmodel_update(cambios)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def eliminar_producto(session: Session, producto: Producto) -> None:
    session.delete(producto)
    session.commit()


def asociar_categoria(
    session: Session,
    producto_id: int,
    categoria_id: int,
) -> ProductoCategoria | None:
    producto = session.get(Producto, producto_id)
    categoria = session.get(Categoria, categoria_id)

    if producto is None or categoria is None:
        return None

    asociacion_existente = session.get(
        ProductoCategoria,
        (producto_id, categoria_id),
    )

    if asociacion_existente is not None:
        return asociacion_existente

    asociacion = ProductoCategoria(
        producto_id=producto_id,
        categoria_id=categoria_id,
    )
    session.add(asociacion)
    session.commit()
    session.refresh(asociacion)
    return asociacion


def listar_categorias_producto(
    session: Session,
    producto_id: int,
) -> list[Categoria] | None:
    producto = session.get(Producto, producto_id)

    if producto is None:
        return None

    consulta = (
        select(Categoria)
        .join(
            ProductoCategoria,
            ProductoCategoria.categoria_id == Categoria.id,
        )
        .where(ProductoCategoria.producto_id == producto_id)
    )

    return session.exec(consulta).all()


def desasociar_categoria(
    session: Session,
    producto_id: int,
    categoria_id: int,
) -> bool:
    asociacion = session.get(
        ProductoCategoria,
        (producto_id, categoria_id),
    )

    if asociacion is None:
        return False

    session.delete(asociacion)
    session.commit()
    return True
