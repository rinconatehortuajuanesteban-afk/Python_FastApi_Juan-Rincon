from fastapi import APIRouter, HTTPException

from app.modelos.clientes import Cliente
from app.conexion_bd import clientes

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.post("")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)

    return {
        "mensaje": "Cliente creado",
        "cliente": cliente
    }


@router.get("")
def obtener_clientes():
    return clientes


@router.get("/{cliente_id}")
def obtener_cliente(cliente_id: int):

    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )


@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int,
                        cliente_actualizado: Cliente):

    for i, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            clientes[i] = cliente_actualizado

            return {
                "mensaje": "Cliente actualizado",
                "cliente": cliente_actualizado
            }

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )


@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):

    for i, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            clientes.pop(i)

            return {
                "mensaje": "Cliente eliminado"
            }

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )