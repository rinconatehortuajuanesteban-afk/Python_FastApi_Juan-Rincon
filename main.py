from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ======================================
# MODELOS
# ======================================

# CLIENTES
class Cliente(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: str


# FACTURAS
class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente_id: int


# TRANSACCIONES
class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int


# ======================================
# BASE DE DATOS TEMPORAL
# ======================================

clientes = []
facturas = []
transacciones = []


# ======================================
# CLIENTES CRUD
# ======================================

@app.post("/clientes")
def crear_cliente(cliente: Cliente):

    clientes.append(cliente)

    return {
        "mensaje": "Cliente creado",
        "cliente": cliente
    }


@app.get("/clientes")
def obtener_clientes():
    return clientes


@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):

    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente_actualizado: Cliente):

    for index, cliente in enumerate(clientes):

        if cliente.id == cliente_id:
            clientes[index] = cliente_actualizado

            return {
                "mensaje": "Cliente actualizado",
                "cliente": cliente_actualizado
            }

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):

    for index, cliente in enumerate(clientes):

        if cliente.id == cliente_id:
            clientes.pop(index)

            return {
                "mensaje": "Cliente eliminado"
            }

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ======================================
# FACTURAS CRUD
# ======================================

@app.post("/facturas")
def crear_factura(factura: Factura):

    facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }


@app.get("/facturas")
def obtener_facturas():
    return facturas


@app.get("/facturas/{factura_id}")
def obtener_factura(factura_id: int):

    for factura in facturas:
        if factura.id == factura_id:
            return factura

    raise HTTPException(status_code=404, detail="Factura no encontrada")


@app.put("/facturas/{factura_id}")
def actualizar_factura(factura_id: int, factura_actualizada: Factura):

    for index, factura in enumerate(facturas):

        if factura.id == factura_id:
            facturas[index] = factura_actualizada

            return {
                "mensaje": "Factura actualizada",
                "factura": factura_actualizada
            }

    raise HTTPException(status_code=404, detail="Factura no encontrada")


@app.delete("/facturas/{factura_id}")
def eliminar_factura(factura_id: int):

    for index, factura in enumerate(facturas):

        if factura.id == factura_id:
            facturas.pop(index)

            return {
                "mensaje": "Factura eliminada"
            }

    raise HTTPException(status_code=404, detail="Factura no encontrada")


# ======================================
# TRANSACCIONES CRUD
# ======================================

@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):

    transacciones.append(transaccion)

    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion
    }


@app.get("/transacciones")
def obtener_transacciones():
    return transacciones


@app.get("/transacciones/{transaccion_id}")
def obtener_transaccion(transaccion_id: int):

    for transaccion in transacciones:
        if transaccion.id == transaccion_id:
            return transaccion

    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@app.put("/transacciones/{transaccion_id}")
def actualizar_transaccion(transaccion_id: int, transaccion_actualizada: Transaccion):

    for index, transaccion in enumerate(transacciones):

        if transaccion.id == transaccion_id:
            transacciones[index] = transaccion_actualizada

            return {
                "mensaje": "Transacción actualizada",
                "transaccion": transaccion_actualizada
            }

    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@app.delete("/transacciones/{transaccion_id}")
def eliminar_transaccion(transaccion_id: int):

    for index, transaccion in enumerate(transacciones):

        if transaccion.id == transaccion_id:
            transacciones.pop(index)

            return {
                "mensaje": "Transacción eliminada"
            }

    raise HTTPException(status_code=404, detail="Transacción no encontrada")