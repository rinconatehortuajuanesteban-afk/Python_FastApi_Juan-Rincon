from fastapi import APIRouter, HTTPException
from models import Transaccion
from database import transacciones

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


@router.post("")
def crear_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion
    }


@router.get("")
def obtener_transacciones():
    return transacciones


@router.get("/{transaccion_id}")
def obtener_transaccion(transaccion_id: int):

    for transaccion in transacciones:
        if transaccion.id == transaccion_id:
            return transaccion

    raise HTTPException(
        status_code=404,
        detail="Transacción no encontrada"
    )


@router.put("/{transaccion_id}")
def actualizar_transaccion(
    transaccion_id: int,
    transaccion_actualizada: Transaccion
):

    for index, transaccion in enumerate(transacciones):

        if transaccion.id == transaccion_id:
            transacciones[index] = transaccion_actualizada

            return {
                "mensaje": "Transacción actualizada",
                "transaccion": transaccion_actualizada
            }

    raise HTTPException(
        status_code=404,
        detail="Transacción no encontrada"
    )


@router.delete("/{transaccion_id}")
def eliminar_transaccion(transaccion_id: int):

    for index, transaccion in enumerate(transacciones):

        if transaccion.id == transaccion_id:
            transacciones.pop(index)

            return {
                "mensaje": "Transacción eliminada"
            }

    raise HTTPException(
        status_code=404,
        detail="Transacción no encontrada"
    )