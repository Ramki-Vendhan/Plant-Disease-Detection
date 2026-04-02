from fastapi.responses import JSONResponse
import requests
import json
from datetime import datetime

def get_weather(lat: float, lon: float):
    print(lat, lon)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    
    with open("weather_code.json", 'r') as file:
        weather_codes = json.load(file)
    
    weather_data = {
        "location": f"Lat: {lat}, Lon: {lon}",
        "temperature": data["current_weather"]["temperature"],
        "weather": weather_codes.get(str(data["current_weather"]["weathercode"]), "unknown"),
        "timestamp": datetime.now().isoformat()
    }
    
    with open('weather_data.json', 'w') as json_file:
        json.dump(weather_data, json_file, indent = 2)
        json_file.write('\n')

    return weather_data