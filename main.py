from fastapi import FastAPI

# 👇 THIS VARIABLE NAME MUST BE "app"
app = FastAPI(title="Weather App (Dummy Data)")

weather_data = {
    "delhi": {
        "temperature": 35,
        "condition": "Sunny",
        "humidity": 40
    },
    "london": {
        "temperature": 18,
        "condition": "Cloudy",
        "humidity": 65
    },
    "newyork": {
        "temperature": 22,
        "condition": "Rainy",
        "humidity": 70
    },
    "tokyo": {
        "temperature": 27,
        "condition": "Clear",
        "humidity": 55
    }
}

@app.get("/")
def home():
    return {"message": "Dummy Weather API is running ☀️"}

@app.get("/weather")
def all_weather():
    return weather_data

@app.get("/weather/{city}")
def get_weather(city: str):
    city = city.lower()
    if city in weather_data:
        return {"city": city, "weather": weather_data[city]}
    return {"error": "City not found"}
