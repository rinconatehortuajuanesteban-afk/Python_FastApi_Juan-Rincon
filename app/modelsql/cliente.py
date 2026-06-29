from sqlalchemy import Column, Integer, String

from app.conexion_bd import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    telefono = Column(String(50))