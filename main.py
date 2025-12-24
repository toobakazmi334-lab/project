from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Weather App GUI")

# ---------------- DUMMY WEATHER DATA ----------------
weather_data = {
    "delhi": {"temperature": 35, "condition": "Sunny", "humidity": 40},
    "london": {"temperature": 18, "condition": "Cloudy", "humidity": 65},
    "newyork": {"temperature": 22, "condition": "Rainy", "humidity": 70},
    "tokyo": {"temperature": 27, "condition": "Clear", "humidity": 55},
}

# ---------------- GUI HOME PAGE ----------------
@app.get("/", response_class=HTMLResponse)
def home():
    city_cards = ""
    for city, data in weather_data.items():
        city_cards += f"""
        <div class="card">
            <h2>{city.title()}</h2>
            <p>🌡 Temperature: {data['temperature']}°C</p>
            <p>🌤 Condition: {data['condition']}</p>
            <p>💧 Humidity: {data['humidity']}%</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #74ebd5, #9face6);
                text-align: center;
                padding: 40px;
            }}
            h1 {{
                color: #fff;
                margin-bottom: 30px;
            }}
            .container {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
            }}
            .card {{
                background: white;
                padding: 20px;
                width: 220px;
                border-radius: 12px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }}
            .card h2 {{
                margin-bottom: 10px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <h1>🌦 Dummy Weather App</h1>
        <div class="container">
            {city_cards}
        </div>
    </body>
    </html>
    """

# ---------------- API ENDPOINT ----------------
@app.get("/api/weather")
def api_weather():
    return weather_data
