from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from datetime import datetime
from remedy import get_remedy_for_disease
from find_weather import get_weather
from detect import predict_disease
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Allow CORS from any origin (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

templates = Jinja2Templates(directory="templates")

@app.post("/disease")
async def upload(file: UploadFile = File(...), lat: float = Form(...), lon: float = Form(...)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    disease = predict_disease(file_path)

    weather_data = get_weather(lat, lon)
    weather_details = f"{weather_data["location"]}, temperature {weather_data["temperature"]} C, weather is {weather_data["weather"]}, at {weather_data["timestamp"]}"
    print(weather_details)

    remedy = get_remedy_for_disease(disease , weather_details)

    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)

    result_data = {
        "disease" : disease,
        "remedy" : remedy
    }

    print(result_data)

    return JSONResponse(content = result_data)