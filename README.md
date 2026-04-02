# Plant-Disease-Detection
🌱 Plant Disease Detection System An AI-based web application that detects plant diseases from leaf images and provides appropriate remedies. It helps in early diagnosis, reduces crop loss, and supports smart agriculture using machine learning and FastAPI.

📖 Overview

The Plant Disease Detection System helps farmers and agriculture enthusiasts identify plant diseases at an early stage using image classification. Users can upload a leaf image, and the system predicts the disease and suggests appropriate treatments.

✨ Features
🌿 Upload plant leaf images
🤖 AI-based disease prediction
📊 Displays disease name and details
💊 Provides remedies and prevention tips
🌐 Simple and user-friendly interface

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: FastAPI (Python)
Machine Learning: TensorFlow / Keras
Other Tools: OpenCV, Git, GitHub

⚙️ How It Works
User uploads a plant leaf image
Image is sent to the backend (FastAPI)
ML model processes the image
Disease is predicted
Result with remedy is displayed

📁 Project Structure
plant-disease-detection/
│
├── templates/        # HTML files
├── static/           # CSS, JS, images
├── model/            # Trained ML model
├── main.py           # Backend (FastAPI)
├── list_models.py    # Model handling
├── README.md

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/your-username/plant-disease-detection.git

cd plant-disease-detection

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the project
uvicorn main:app --reload

4️⃣ Open in browser
http://127.0.0.1:8000

🔮 Future Improvements
📱 Mobile application support
🌍 Multi-language support
☁️ Cloud deployment
📍 Nearby agricultural shop integration
🌦️ Weather-based predictions
