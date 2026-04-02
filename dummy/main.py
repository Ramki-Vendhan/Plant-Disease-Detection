from fastapi import FastAPI, Form, Request,File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detect import predict_disease
from typing import List
import geocoder
import math
import shutil,os
from dotenv import load_dotenv
from PIL import Image
import os
import json
import google.generativeai as genai
from fastapi import UploadFile
from remedy import get_remedy_for_disease


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

app = FastAPI()

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# CORS for JS-based frontend interactions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ------------------------------
# Disease Remedy Feature
# ------------------------------
# Route for handling the form submission
@app.post("/disease", response_class=HTMLResponse)
async def detect_dieseas(request: Request, imag: str = Form(...)):
    # Save the uploaded image
    image_path = f"temp_{image.filename}"
    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    # Predict disease
    disease = predict_disease(image_path)
    os.remove(image_path)

    weather_info = "Lat: 10.6867, Lon: 78.6155, temperature 28.5 C, weather is Overcast"
    remedy = get_remedy_for_disease(disease, weather_info)


    #emedy = get_remedy_for_disease(disease_name)
    
    return templates.TemplateResponse(".html", {
        "request": request,
        "disease_name": disease,
        "remedy": remedy["remedy"]
    })
    #return templates.TemplateResponse("theme_change.html", {
    #"request": request,
    #"disease_name": disease,
    #"remedy": remedy["remedy"]  # this should be a list of dicts with remedy_name and description
#})

#fetchlocation

@app.get("/fetloc", response_class=HTMLResponse)
def get_location(request: Request):
    return templates.TemplateResponse("fetloc.html", {"request": request})

# ------------------------------
# Live Location Page
# ------------------------------
@app.get("/live-location", response_class=HTMLResponse)
def show_live_location(request: Request):
    g = geocoder.ip('me')
    if g.ok and g.latlng:
        latitude, longitude = g.latlng
    else:
        latitude, longitude = "Unknown", "Unknown"

    return templates.TemplateResponse("livloc.html", {
        "request": request,
        "latitude": latitude,
        "longitude": longitude
    })

# ------------------------------
# Nearby Shops (API + Page)
# ------------------------------
class Shop(BaseModel):
    name: str
    latitude: float
    longitude: float
    category: str
    image: str



def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

@app.get("/shops", response_class=HTMLResponse)
def nearby_shops(request: Request):
    return templates.TemplateResponse("nearbyshop.html", {"request": request})

@app.post("/nearby-shops/")
async def get_nearby_shops(request: Request):
    data = await request.json()
    user_lat = data["latitude"]
    user_lon = data["longitude"]
    nearby = []

    for shop in shops_db:
        dist = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
        if dist <= 5:
            nearby.append({
                "name": shop.name,
                "category": shop.category,
                "distance": round(dist, 2),
                "image": shop.image
            })
    return {"shops": nearby}

# ------------------------------
# Contact Page
# ------------------------------
@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

    
