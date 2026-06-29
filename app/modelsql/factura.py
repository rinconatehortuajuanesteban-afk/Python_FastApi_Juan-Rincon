from sqlalchemy import Column, Integer, Float, String

from app.conexion_bd import Base


class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(String(20))
    valor_total = Column(Float)
    cliente_id = Column(Integer)