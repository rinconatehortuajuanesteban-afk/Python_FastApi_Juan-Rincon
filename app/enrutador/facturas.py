from fastapi import APIRouter, HTTPException

from app.modelos.facturas import Factura
from app.conexion_bd import facturas

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)


@router.post("")
def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }


@router.get("")
def obtener_facturas():
    return facturas


@router.get("/{factura_id}")
def obtener_factura(factura_id: int):

    for factura in facturas:
        if factura.id == factura_id:
            return factura

    raise HTTPException(
        status_code=404,
        detail="Factura no encontrada"
    )


@router.put("/{factura_id}")
def actualizar_factura(
    factura_id: int,
    factura_actualizada: Factura
):

    for index, factura in enumerate(facturas):

        if factura.id == factura_id:
            facturas[index] = factura_actualizada

            return {
                "mensaje": "Factura actualizada",
                "factura": factura_actualizada
            }

    raise HTTPException(
        status_code=404,
        detail="Factura no encontrada"
    )


@router.delete("/{factura_id}")
def eliminar_factura(factura_id: int):

    for index, factura in enumerate(facturas):

        if factura.id == factura_id:
            facturas.pop(index)

            return {
                "mensaje": "Factura eliminada"
            }

    raise HTTPException(
        status_code=404,
        detail="Factura no encontrada"
    )