from fastapi import FastAPI

from app.enrutador.clientes import router as clientes_router
from app.enrutador.facturas import router as facturas_router
from app.enrutador.transacciones import router as transacciones_router

app = FastAPI()

app.include_router(clientes_router, tags=["Clientes"], prefix="/clientes")
app.include_router(facturas_router, tags=["Facturas"], prefix="/facturas")
app.include_router(transacciones_router, tags=["Transacciones"], prefix="/transacciones")