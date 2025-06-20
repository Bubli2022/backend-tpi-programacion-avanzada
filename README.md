# Weather App - Backend

Trabajo Práctico Integrador  
Alumnos:

-  Lautaro Vergara (DNI 47307319)
-  Ignacio Heredia (DNI 47064312)
-  Ariel Marcos Perez (DNI 29122141)

---

## Descripción

Este es el backend de la aplicación Weather App, desarrollado con **Python** utilizando el framework **FastAPI**. Su función es actuar como intermediario entre el frontend y la API externa de OpenWeatherMap, permitiendo obtener datos del clima actual mediante solicitudes HTTP.

---

## Tecnologías

-  Python 3.11
-  FastAPI
-  Uvicorn (servidor ASGI)
-  HTTPX (cliente HTTP asíncrono)
-  python-dotenv (lectura de variables de entorno)
-  OpenWeatherMap API

---

Enlaces de weather app del tpi de programación avanzada:

Enlace conectado en linea a través de Netlify del frontend:
https://tpi-programacion-avanzada.netlify.app/

Tecnologías usadas Frontend: React, Javascript, Axios, CSS/HTML, API personalizada (FastAPI - Python)

Enlace conectado en linea a traves de Render del backend:

https://backend-tpi-programacion-avanzada.onrender.com/docs

Tecnologías usadas Backend: Python, FastAPI, Uvicorn, HTTPX, python-dotenv, OpenWeatherMap API

Repositorios de GitHub:

Frontend:
https://github.com/Bubli2022/frontend-tpi-programacion-avanzada.git

Backend:
https://github.com/Bubli2022/backend-tpi-programacion-avanzada.git

## Instalación

### 1. Clonar el repositorio y acceder a la carpeta `backend`:

`````bash
git clone https://github.com/Bubli2022/backend-tpi-programacion-avanzada.git
cd backend

###2. Crear entorno virtual (recomendado):
```bash

python -m venv venv

# 3. Activar el entorno virtual:
# En PowerShell (Windows):

```bash

venv\Scripts\Activate.ps1

# En Git Bash:

```bash

source venv/Scripts/activate

# 4. Instalar dependencias:
```bash

pip install -r requirements.txt

# Si no tenés el archivo requirements.txt, podés instalar manualmente con:

```bash

pip install fastapi uvicorn httpx python-dotenv

# Configuración
# Crear un archivo .env en la carpeta backend con el siguiente contenido:

```env
Copiar código
OPENWEATHER_API_KEY=TU_CLAVE_DE_API

# Reemplazar TU_CLAVE_DE_API con la clave real de OpenWeatherMap.

# ```Ejecución
# Con el entorno virtual activado, ejecutar el servidor FastAPI con:

```bash

python -m uvicorn main:app --reload
# El backend estará disponible en:

arduino

http://localhost:8000

# Endpoints
# GET /weather?city=NombreCiudad: Devuelve los datos climáticos actuales de la ciudad indicada.

# Ejemplo:

```bash
# Copiar código
http://localhost:8000/weather?city=Buenos%20Aires

# Notas
# Es necesario tener conexión a internet para acceder a los datos climáticos externos.

# El backend debe estar corriendo antes de iniciar el frontend.

# Se recomienda no exponer la clave de API públicamente.

# Licencia
# Este proyecto fue desarrollado con fines académicos para la materia Programación Avanzada en la Universidad Nacional Almirante Brown.
# ````
`````
