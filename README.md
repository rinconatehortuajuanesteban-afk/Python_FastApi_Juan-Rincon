# 🚀 API REST de Gestión de Clientes, Facturas y Transacciones

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Architecture](https://img.shields.io/badge/Architecture-Modular-orange)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-yellow)

---

## 📌 Descripción del Proyecto

Este proyecto es una **API REST modular** desarrollada con FastAPI, orientada a la gestión de:

- 👤 Clientes  
- 🧾 Facturas  
- 💳 Transacciones  

El sistema implementa una arquitectura **separada por capas**, lo que permite escalabilidad, mantenimiento sencillo y claridad en la lógica del negocio.

Actualmente, la persistencia de datos puede manejarse en memoria o mediante una futura integración con base de datos relacional.

---

## 🧠 Arquitectura General del Sistema

La API está diseñada bajo un enfoque modular:

```
Cliente (Frontend / Postman)
        ↓
Enrutadores (app/enrutador/)
        ↓
Validación de datos (app/modelos/)
        ↓
Lógica / almacenamiento (conexion_bd.py)
        ↓
Respuesta JSON (FastAPI)
```

---

## 🧱 Estructura del Proyecto

```text
PYTHON_JUAN_RINCON/
│
├── app/
│   ├── main.py                  # Punto de entrada de la aplicación
│   ├── conexion_bd.py          # Capa de acceso a datos (memoria o BD futura)
│   │
│   ├── modelos/                # Definición de esquemas (Pydantic)
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   └── enrutador/              # Definición de endpoints (API REST)
│       ├── clientes.py
│       ├── facturas.py
│       └── transacciones.py
│
├── requirements.txt           # Dependencias del proyecto
├── README.md
└── .gitignore
```

---

## ⚙️ Tecnologías Utilizadas

- Python 3.12 🐍  
- FastAPI ⚡ (Framework web moderno y de alto rendimiento)  
- Pydantic 📐 (Validación de datos y esquemas)  
- Uvicorn 🚀 (Servidor ASGI)  
- Swagger UI 📚 (Documentación automática interactiva)  
- ReDoc 📄 (Documentación alternativa)

---

## 🧩 Arquitectura por Capas

### 1. 📌 main.py (Capa de inicialización)

Responsable de:

- Crear la aplicación FastAPI
- Registrar los routers
- Configurar la API global

📌 Traducción técnica:

> Es el punto de arranque del sistema. Aquí se ensamblan todos los módulos.

---

### 2. 📌 enrutador/ (Capa de control - API Layer)

Contiene los endpoints que exponen la funcionalidad del sistema.

Cada archivo representa un dominio:

- clientes.py → gestión de clientes
- facturas.py → gestión de facturación
- transacciones.py → operaciones financieras

📌 Traducción técnica:

> Es la capa que recibe solicitudes HTTP y decide qué hacer con ellas.

---

### 3. 📌 modelos/ (Capa de validación)

Define la estructura de los datos usando Pydantic.

Ejemplo de cliente:

```json
{
  "id": 1,
  "nombre": "Juan",
  "correo": "juan@email.com"
}
```

📌 Traducción técnica:

> Actúa como un filtro: solo deja pasar datos válidos y bien estructurados.

---

### 4. 📌 conexion_bd.py (Capa de datos)

Responsable de:

- Simular almacenamiento en memoria
- Preparar futura conexión a base de datos
- Centralizar acceso a datos

📌 Traducción técnica:

> Es la memoria del sistema o el puente hacia una base de datos real.

---

## 🔁 Flujo de una petición

Ejemplo: `POST /clientes`

```
1. Cliente envía request HTTP
2. Enrutador recibe la solicitud
3. Modelo valida los datos
4. conexion_bd procesa o almacena información
5. FastAPI responde en JSON
```

---

## 🧪 Ejemplo de Uso

### ➤ Request

```json
POST /clientes
{
  "nombre": "Ana Pérez",
  "correo": "ana@email.com"
}
```

### ➤ Response

```json
{
  "mensaje": "Cliente creado correctamente",
  "id": 1
}
```

---

## 🚀 Instalación del Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/rinconatehortuajuanesteban-afk/Python_FastApi_Juan-Rincon.git
cd Python_FastApi_Juan-Rincon
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar entorno virtual

#### Windows (CMD)
```bash
venv\Scripts\activate.bat
```

#### Windows (PowerShell)
```powershell
.\venv\Scripts\Activate.ps1
```

#### Linux / Mac
```bash
source venv/bin/activate
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 5. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

---

### 6. Acceder a la API

- API principal:
```
http://127.0.0.1:8000
```

- Documentación Swagger:
```
http://127.0.0.1:8000/docs
```

- Documentación ReDoc:
```
http://127.0.0.1:8000/redoc
```

---

## ⚠️ Limitaciones del Sistema

- No cuenta con base de datos persistente
- No incluye autenticación ni autorización
- No hay control de duplicidad de registros
- Validaciones de relaciones aún básicas

---

## 🔮 Mejoras Futuras

- 🗄️ Integración con PostgreSQL o MySQL  
- 🧱 ORM (SQLAlchemy)  
- 🔐 Autenticación JWT  
- 🐳 Contenerización con Docker  
- 🧪 Pruebas unitarias e integración  
- 📊 Sistema de logs y auditoría  
- ⚡ Optimización de rendimiento  

---

## 🧑‍💻 Autor

**Juan Esteban Rincón Atehortúa**

> “La ingeniería no es solo escribir código, es diseñar sistemas que sobrevivan al tiempo.”

---

## 🧠 Reflexión técnica

Una API no es solo un conjunto de rutas.

Es un sistema vivo compuesto por reglas, datos y decisiones.

- Los modelos definen la forma del mundo  
- Los routers definen cómo se interactúa con él  
- La lógica define su comportamiento  

Este proyecto es una base sólida para sistemas escalables reales.