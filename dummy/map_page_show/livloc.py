import geocoder
import webbrowser
import os

# Get user location
g = geocoder.ip('me')
if g.ok and g.latlng:
    latitude, longitude = g.latlng
else:
    print("❌ Could not fetch your location.")
    exit()

# HTML with link to next page
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Your Live Location</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(120deg, #d4fc79, #96e6a1);
            height: 100vh;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        h1 {{
            color: #2e7d32;
            font-size: 3rem;
        }}
        p {{
            font-size: 20px;
        }}
        a {{
            margin-top: 20px;
            padding: 12px 25px;
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            transition: background 0.3s;
        }}
        a:hover {{
            background-color: #388e3c;
        }}
    </style>
</head>
<body>
    <h1>📍 Your Live Location</h1>
    <p>Latitude: {latitude}</p>
    <p>Longitude: {longitude}</p>
    <a href="nearby_agri_shops.html">Go to Nearby Agri Shops 🚜</a>
</body>
</html>
"""

# Save it
with open("templates/livloc.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Open in browser
webbrowser.open("file://" + os.path.abspath("live_location.html"))
print("✅ Live location page created and opened!")



import webbrowser
import os
import time

html_file = "fetching_location.html"

print("🚀 Launching Location Fetching Page...")

if os.path.exists(html_file):
    webbrowser.open('file://' + os.path.realpath(html_file))
else:
    print("❌ Error: File not found!")




import webbrowser
import os
webbrowser.open("file://" + os.path.abspath("live_location.html"))
print("✅ Live location page created and opened!")


import webbrowser
import os
import time
print("\n🚀 Starting Live Location Detector...")
time.sleep(1)
print("🔍 Fetching HTML file...")
time.sleep(1)

html_file = "templates/livloc.html"  # Make sure this file exists

if os.path.exists(html_file):
    webbrowser.open('file://' + os.path.realpath(html_file))
    print("✅ Opened successfully! Enjoy!")
else:
    print("❌ Error: File not found!")
