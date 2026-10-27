
from sqlmodel import Session, select

from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate


def listar_categorias(session: Session) -> list[Categoria]:
    statement = select(Categoria).order_by(Categoria.id)
    return list(session.exec(statement).all())


def obtener_categoria(session: Session, categoria_id: int) -> Categoria | None:
    return session.get(Categoria, categoria_id)


def crear_categoria(session: Session, datos: CategoriaCreate) -> Categoria:
    categoria = Categoria.model_validate(datos)

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def actualizar_categoria(
    session: Session,
    categoria: Categoria,
    datos: CategoriaUpdate,
) -> Categoria:
    cambios = datos.model_dump(exclude_unset=True, exclude_none=True)

    categoria.sqlmodel_update(cambios)

    session.add(categoria)
    session.commit()
    session.refresh(categoria)

    return categoria


def eliminar_categoria(session: Session, categoria: Categoria) -> None:
    session.delete(categoria)
    session.commit()
