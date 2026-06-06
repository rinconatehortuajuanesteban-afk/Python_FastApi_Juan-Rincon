# API de Gestión de Clientes, Facturas y Transacciones

## Descripción

Esta aplicación es una API REST desarrollada con **FastAPI** que permite realizar operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) sobre tres entidades principales:

* Clientes
* Facturas
* Transacciones

La información se almacena temporalmente en memoria mediante listas de Python, por lo que los datos se pierden al reiniciar la aplicación.

---

## Tecnologías Utilizadas

* Python 3.10+
* FastAPI
* Pydantic
* Uvicorn

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv venv
```

Activar entorno virtual:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install fastapi uvicorn
```

---

## Ejecución del Proyecto

Ejecutar el servidor con:

```bash
uvicorn main:app --reload
```

Donde:

* `main` corresponde al nombre del archivo Python.
* `app` es la instancia de FastAPI.

La API estará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación Automática

FastAPI genera documentación automáticamente.

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

### Campos

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

### Campos

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

### Campos

| Campo       | Tipo  |
| ----------- | ----- |
| id          | int   |
| vr_unitario | float |
| cantidad    | int   |
| factura_id  | int   |

---

# Endpoints

## Clientes

### Crear cliente

```http
POST /clientes
```

### Obtener todos los clientes

```http
GET /clientes
```

### Obtener cliente por ID

```http
GET /clientes/{cliente_id}
```

### Actualizar cliente

```http
PUT /clientes/{cliente_id}
```

### Eliminar cliente

```http
DELETE /clientes/{cliente_id}
```

---

## Facturas

### Crear factura

```http
POST /facturas
```

### Obtener todas las facturas

```http
GET /facturas
```

### Obtener factura por ID

```http
GET /facturas/{factura_id}
```

### Actualizar factura

```http
PUT /facturas/{factura_id}
```

### Eliminar factura

```http
DELETE /facturas/{factura_id}
```

---

## Transacciones

### Crear transacción

```http
POST /transacciones
```

### Obtener todas las transacciones

```http
GET /transacciones
```

### Obtener transacción por ID

```http
GET /transacciones/{transaccion_id}
```

### Actualizar transacción

```http
PUT /transacciones/{transaccion_id}
```

### Eliminar transacción

```http
DELETE /transacciones/{transaccion_id}
```

---

# Ejemplo de Uso

### Crear un Cliente

**Solicitud**

```http
POST /clientes
```

```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "correo": "juan@email.com",
  "telefono": "3001234567"
}
```

**Respuesta**

```json
{
  "mensaje": "Cliente creado",
  "cliente": {
    "id": 1,
    "nombre": "Juan Pérez",
    "correo": "juan@email.com",
    "telefono": "3001234567"
  }
}
```

---

# Manejo de Errores

Cuando un recurso no existe, la API responde con:

```json
{
  "detail": "Cliente no encontrado"
}
```

Código HTTP:

```http
404 Not Found
```

---

# Limitaciones Actuales

* No existe persistencia en base de datos.
* Los datos se almacenan únicamente en memoria.
* No se valida la existencia de clientes antes de crear facturas.
* No se valida la existencia de facturas antes de crear transacciones.
* No existe autenticación ni autorización.
* No se controlan registros duplicados.

---

# Mejoras Futuras

* Integración con PostgreSQL o MySQL.
* Uso de SQLAlchemy.
* Implementación de autenticación JWT.
* Validación de relaciones entre entidades.
* Paginación de resultados.
* Registro de auditoría y logs.
* Pruebas unitarias y de integración.
* Despliegue mediante Docker.

---

## Autor

Proyecto desarrollado como práctica de construcción de APIs REST utilizando FastAPI y Pydantic.
