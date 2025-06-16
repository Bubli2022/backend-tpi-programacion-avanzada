from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplazar por el dominio frontend
    allow_credentials=True,
    allow_methods=["GET"],  # Métodos HTTP permitidos
    allow_headers=["*"],
)

@app.get("/weather/city")
def get_weather_by_city(city: str = Query(...)):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Ciudad no encontrada")
    return response.json()

@app.get("/weather/coordinates")
def get_weather_by_coords(lat: float = Query(...), lon: float = Query(...)):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Coordenadas inválidas")
    return response.json()
