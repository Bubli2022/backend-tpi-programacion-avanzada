# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
from dotenv import load_dotenv
import requests

# Cargar variables del archivo .env
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()

# Configurar CORS para permitir que el frontend acceda al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés reemplazar "*" por tu dominio en producción
    allow_credentials=True,
    allow_methods=["http://localhost:3000"],
    allow_headers=["*"],
)

@app.get("/weather")
async def get_weather(city: str = Query(...)):
    """Consulta el clima para una ciudad dada"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response.json()

@app.get("/weather/coordinates")
def get_weather_by_coords(lat: float = Query(...), lon: float = Query(...)):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}"
        f"&appid={API_KEY}&units=metric"
    )
    response = requests.get(url)
    return response.json()