# API de Gestión de Clientes, Facturas y Transacciones

## Descripción General

Este proyecto consiste en una API REST desarrollada con **FastAPI**, diseñada para gestionar información relacionada con clientes, facturas y transacciones mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar).

La aplicación permite administrar cada entidad a través de endpoints HTTP y utiliza modelos de datos definidos con **Pydantic** para validar la información recibida.

Actualmente, los datos se almacenan en memoria mediante listas de Python, por lo que no existe persistencia permanente y la información se pierde al reiniciar la aplicación.

---

## Tecnologías Utilizadas

* Python 3.12
* FastAPI
* Pydantic
* Uvicorn
* Swagger UI
* ReDoc

---

## Características Principales

* Gestión de clientes.
* Gestión de facturas.
* Gestión de transacciones.
* Validación automática de datos.
* Documentación interactiva generada automáticamente.
* Arquitectura basada en servicios REST.
* Respuestas en formato JSON.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/rinconatehortuajuanesteban-afk/Python_FastApi_Juan-Rincon.git
cd Python_FastApi_Juan-Rincon
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

#### Windows (CMD)

```bash
venv\Scripts\activate.bat
```

#### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

#### Git Bash

```bash
source venv/Scripts/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución del Proyecto

Iniciar el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

Donde:

* `main` corresponde al archivo principal de la aplicación.
* `app` corresponde a la instancia de FastAPI.

Una vez iniciado el servidor, la aplicación estará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación de la API

FastAPI genera documentación automática para facilitar las pruebas y el consumo de los servicios.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Modelos de Datos

## Cliente

```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@email.com",
  "telefono": "3001234567"
}
```

| Campo    | Tipo   |
| -------- | ------ |
| id       | int    |
| nombre   | string |
| correo   | string |
| telefono | string |

---

## Factura

```json
{
  "id": 1,
  "fecha": "2025-01-15",
  "valor_total": 500000,
  "cliente_id": 1
}
```

| Campo       | Tipo   |
| ----------- | ------ |
| id          | int    |
| fecha       | string |
| valor_total | float  |
| cliente_id  | int    |

---

## Transacción

```json
{
  "id": 1,
  "vr_unitario": 25000,
  "cantidad": 4,
  "factura_id": 1
}
```

| Campo       | Tipo  |
| ----------- | ----- |
| id          | int   |
| vr_unitario | float |
| cantidad    | int   |
| factura_id  | int   |

---

# Endpoints Disponibles

## Clientes

| Método | Endpoint               | Descripción                |
| ------ | ---------------------- | -------------------------- |
| POST   | /clientes              | Crear cliente              |
| GET    | /clientes              | Obtener todos los clientes |
| GET    | /clientes/{cliente_id} | Obtener cliente por ID     |
| PUT    | /clientes/{cliente_id} | Actualizar cliente         |
| DELETE | /clientes/{cliente_id} | Eliminar cliente           |

---

## Facturas

| Método | Endpoint               | Descripción                |
| ------ | ---------------------- | -------------------------- |
| POST   | /facturas              | Crear factura              |
| GET    | /facturas              | Obtener todas las facturas |
| GET    | /facturas/{factura_id} | Obtener factura por ID     |
| PUT    | /facturas/{factura_id} | Actualizar factura         |
| DELETE | /facturas/{factura_id} | Eliminar factura           |

---

## Transacciones

| Método | Endpoint                        | Descripción                     |
| ------ | ------------------------------- | ------------------------------- |
| POST   | /transacciones                  | Crear transacción               |
| GET    | /transacciones                  | Obtener todas las transacciones |
| GET    | /transacciones/{transaccion_id} | Obtener transacción por ID      |
| PUT    | /transacciones/{transaccion_id} | Actualizar transacción          |
| DELETE | /transacciones/{transaccion_id} | Eliminar transacción            |

---

## Estructura del Proyecto

```text
Python_FastApi_Juan-Rincon/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── __pycache__/
```

---

## Limitaciones Actuales

* La información se almacena únicamente en memoria.
* No existe persistencia en base de datos.
* No se implementa autenticación de usuarios.
* No se validan relaciones entre entidades.
* No existe control de registros duplicados.

---

## Mejoras Futuras

* Integración con PostgreSQL o MySQL.
* Implementación de SQLAlchemy.
* Autenticación y autorización mediante JWT.
* Validación de integridad referencial.
* Paginación de resultados.
* Registro de auditoría y logs.
* Pruebas unitarias e integración.
* Contenerización mediante Docker.

---

## Autor

**Juan Esteban Rincón Atehortúa**

Proyecto desarrollado como práctica académica para el aprendizaje de FastAPI, construcción de APIs REST y validación de datos con Pydantic.
