from sqlalchemy import Column, Integer, Float

from app.conexion_bd import Base


class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    vr_unitario = Column(Float)
    cantidad = Column(Integer)
    factura_id = Column(Integer)