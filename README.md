# Lowkey
 
> **Gestión integral del mantenimiento de vehículos**
 
---
 
## Integrantes
 
| Nombre |
|--------|
| Joaquín Nicolás Medrano Escobar |
| José Luis Izquierdo Ruiz |
| Héctor Barba Castilla |
 
---
 
## Descripción del proyecto
 
**Lowkey** es una plataforma web diseñada para facilitar la gestión completa del mantenimiento de vehículos particulares. Permite a los usuarios:
 
- Registrar sus coches con todos los datos relevantes (matrícula, marca, modelo, kilometraje, combustible, etc.).
- Añadir y controlar mantenimientos (cambios de aceite, neumáticos, frenos, ITV, revisiones generales, etc.).
- Llevar un registro detallado de gastos asociados a cada vehículo.
- Visualizar estadísticas y tendencias de gasto, coste medio por vehículo y alertas de próximos mantenimientos.
El proyecto consta de un **frontend** desarrollado con HTML, CSS y JavaScript (vanilla) y un **backend** construido con FastAPI que expone una API RESTful, utilizando MongoDB como base de datos NoSQL.
 
---
 
## Tecnologías utilizadas
 
### Frontend
 
- HTML5
- CSS3 — diseño propio con variables CSS, gradientes y animaciones
- JavaScript vanilla — manejo del DOM, navegación entre pantallas, gestión del carrito de piezas, filtros, etc.
### Backend
 
- Python 3.9+
- [FastAPI](https://fastapi.tiangolo.com/) — framework web para construir APIs
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI
- [PyMongo](https://pymongo.readthedocs.io/) — driver oficial de MongoDB para Python
- [Pydantic](https://docs.pydantic.dev/) — validación y serialización de datos
- [python-dotenv](https://pypi.org/project/python-dotenv/) — gestión de variables de entorno
### Base de datos
 
- [MongoDB Atlas](https://www.mongodb.com/atlas) (opcionalmente local) — base de datos NoSQL orientada a documentos
---
 
## Estructura del proyecto
 
```
proyecto/
├── app/                          # Backend (FastAPI)
│   ├── core/
│   │   └── config.py             # Configuración (lectura de .env)
│   ├── db/
│   │   └── session.py            # Conexión a MongoDB
│   ├── routers/                  # Endpoints de la API
│   │   ├── vehicles.py
│   │   ├── maintenances.py
│   │   ├── expenses.py
│   │   └── dashboard.py
│   ├── schemas/                  # Modelos Pydantic
│   │   ├── vehicle.py
│   │   ├── maintenance.py
│   │   ├── expense.py
│   │   └── dashboard.py
│   ├── services/                 # Lógica de negocio
│   │   ├── vehicle_service.py
│   │   ├── maintenance_service.py
│   │   ├── expense_service.py
│   │   └── dashboard_service.py
│   └── main.py                   # Punto de entrada de la API
├── frontend/                     # Archivos del frontend
│   ├── index.html                # Dashboard principal
│   ├── tienda.html               # Tienda de piezas (catálogo)
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   └── assets/
│       ├── styles/
│       │   ├── styles.css
│       │   ├── tienda.css
│       │   └── logstyle.css
│       ├── app.js                # Lógica del dashboard
│       ├── tienda.js             # Lógica de la tienda (filtros, carrito)
│       ├── logapp.js             # Lógica del login
│       └── registerapp.js        # Lógica del registro
├── .env                          # Variables de entorno (no subir a Git)
├── requirements.txt              # Dependencias de Python
└── README.md                     # Este archivo
```
 
---
 
## Requisitos previos
 
- Python **3.9 o superior** instalado en el sistema.
- MongoDB (local o cuenta en MongoDB Atlas).
- `pip` para instalar dependencias.
- Node.js *(opcional)* — para servir el frontend con `http-server`, o simplemente Python para servir archivos estáticos.
---
 
## Instalación y configuración
 
### 1. Clonar el repositorio
 
```bash
git clone <url-del-repositorio>
cd proyecto
```
 
### 2. Crear y activar un entorno virtual (recomendado)
 
```bash
python -m venv venv
source venv/bin/activate    # En Windows: venv\Scripts\activate
```
 
### 3. Instalar dependencias del backend
 
```bash
pip install -r requirements.txt
```
 
### 4. Configurar variables de entorno
 
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta los valores):
 
**MongoDB Atlas:**
```env
MONGODB_URI=mongodb+srv://<usuario>:<contraseña>@cluster.mongodb.net/?retryWrites=true&w=majority
MONGODB_DB_NAME=lowkey
MONGODB_APP_NAME=LowkeyAPI
MONGODB_SERVER_SELECTION_TIMEOUT_MS=5000
```
 
**MongoDB local:**
```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=lowkey
MONGODB_APP_NAME=LowkeyAPI
MONGODB_SERVER_SELECTION_TIMEOUT_MS=5000
```

---
 
## Ejecución del proyecto
 
### Backend (API)
 
Desde la raíz del proyecto, ejecuta:
 
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
 
La API estará disponible en `http://localhost:8000`.  
La documentación interactiva (Swagger UI) estará en `http://localhost:8000/docs`.
 
### Frontend (servidor estático)
 
Navega a la carpeta `frontend` y sirve los archivos estáticos:
 
**Con Python:**
```bash
cd frontend
python -m http.server 3000
```
 
**Con Node.js (`http-server`):**
```bash
npx http-server . -p 3000
```
 
Accede al frontend en `http://localhost:3000`.
 
---
 
## Usuarios de prueba
 
El sistema incluye tres usuarios predeterminados para acceder al login:
 
| Usuario | Contraseña |
|---------|-----------|
| `jose` | `admin` |
| `joaquin` | `admin` |
| `hector` | `admin` |
 
> También puedes registrarte desde `register.html`. Los usuarios se almacenarán en el `localStorage` del navegador (simulación).
 
---
 
## Endpoints principales de la API
 
### Vehículos
 
| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/api/v1/vehicles` | Lista todos los vehículos |
| `POST` | `/api/v1/vehicles` | Crea un nuevo vehículo |
| `GET` | `/api/v1/vehicles/{vehicle_id}` | Obtiene un vehículo por ID |
| `PUT` | `/api/v1/vehicles/{vehicle_id}` | Actualiza un vehículo |
| `DELETE` | `/api/v1/vehicles/{vehicle_id}` | Elimina un vehículo (y sus mantenimientos/gastos) |
 
### Mantenimientos
 
| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/api/v1/maintenances/{vehicle_id}` | Lista los mantenimientos de un vehículo |
| `POST` | `/api/v1/maintenances` | Crea un nuevo mantenimiento |
| `GET` | `/api/v1/maintenances/{vehicle_id}/recent` | Últimos mantenimientos (timeline) |
| `GET` | `/api/v1/maintenances/{vehicle_id}/upcoming-alert` | Alerta de próximo mantenimiento |
 
### Gastos
 
| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/api/v1/expenses/{vehicle_id}` | Lista los gastos de un vehículo |
| `POST` | `/api/v1/expenses` | Crea un nuevo gasto |
| `GET` | `/api/v1/expenses/{vehicle_id}/monthly-summary` | Resumen de gastos del mes actual |
 
### Dashboard
 
| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/api/v1/dashboard/summary` | Resumen global (vehículos, gastos, mantenimientos pendientes) |
| `GET` | `/api/v1/dashboard/{vehicle_id}` | Resumen por vehículo |
| `GET` | `/api/v1/dashboard/statistics` | Estadísticas (coste medio, tendencias, etc.) |
 
---
 
## CORS
 
El backend tiene configurado CORS para permitir peticiones desde cualquier origen (`allow_origins=["*"]`).