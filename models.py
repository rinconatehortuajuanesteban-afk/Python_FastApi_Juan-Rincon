from pydantic import BaseModel


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