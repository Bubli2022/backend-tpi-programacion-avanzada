from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import requests

# --- Cargar variables de entorno ---
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Validación temprana para asegurar que la API key esté configurada
if not API_KEY:
    raise ValueError("La API key no está configurada en el archivo .env.")

# --- Clase que encapsula la lógica de acceso al servicio externo de clima ---
class WeatherService:
    """
    Aplicación de POO para separar responsabilidades:
    - Esta clase actúa como un objeto que representa el servicio de clima.
    - Sus atributos guardan datos relevantes (API key, URL base).
    - Sus métodos son operaciones que puede realizar el objeto, 
      aquí para obtener datos de clima ya sea por ciudad o coordenadas.
    - Encapsula detalles de cómo se hace la consulta HTTP, ocultando esta complejidad.
    """

    def __init__(self, api_key: str):
        # Atributos: datos que el objeto WeatherService guarda para usar en sus métodos
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_by_city(self, city: str):
        """
        Método: representa una acción que el objeto WeatherService puede realizar.
        - Construye los parámetros para la consulta por ciudad.
        - Hace la petición HTTP.
        - Controla errores lanzando excepciones propias de FastAPI para gestión correcta.
        - Retorna la respuesta JSON completa para que el frontend la procese.
        """
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            # Manejo de error con excepción HTTP que FastAPI usa para respuestas controladas
            raise HTTPException(status_code=response.status_code, detail="Ciudad no encontrada")
        return response.json()  # Retorna un objeto (diccionario) con los datos del clima

    def get_by_coordinates(self, lat: float, lon: float):
        """
        Método similar al anterior, pero para consulta por latitud y longitud.
        Esto demuestra polimorfismo aplicado (mismo concepto: obtener clima,
        pero con diferentes parámetros de entrada).
        """
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Coordenadas inválidas")
        return response.json()

# --- Instancia del objeto WeatherService ---
# Aquí creamos un objeto concreto que usaremos para llamar los métodos y obtener datos
weather_service = WeatherService(API_KEY)

# --- Inicialización de la aplicación FastAPI ---
app = FastAPI()

# --- Middleware para CORS ---
# Permite que el frontend, que puede estar en otro dominio, pueda hacer peticiones al backend
# Aquí configuramos que acepte cualquier origen, en producción debería ser más restrictivo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- Mejorar en producción con URL real del frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --- Endpoints de la API ---
@app.get("/weather/city")
def get_weather_by_city(city: str = Query(...)):
    """
    Endpoint que recibe una ciudad como parámetro de consulta.
    Llama al método correspondiente del objeto weather_service para obtener datos.
    Esto separa claramente la capa de presentación (FastAPI) de la capa de negocio (WeatherService).
    """
    return weather_service.get_by_city(city)

@app.get("/weather/coordinates")
def get_weather_by_coords(lat: float = Query(...), lon: float = Query(...)):
    """
    Endpoint para obtener clima según latitud y longitud.
    Sigue el mismo patrón de delegar la lógica a los métodos del objeto WeatherService.
    """
    return weather_service.get_by_coordinates(lat, lon)
