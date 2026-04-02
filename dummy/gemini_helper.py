import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

def get_remedy_for_disease(disease, weather_details):
    try:
#         prompt = f"""
# Based on the plant disease '{disease}', suggest only natural remedies, biopesticides, and preventive measures. Provide the remedies directly without any additional explanation.
# """
        # prompt = f"""
        # The user is a hobbyist or home gardener who grows plants for fun, often in small spaces like balconies, backyards, or pots. They are not commercial farmers.

        # Based on the plant disease '{}', suggest simple and effective remedies"""

        prompt = f"""
        The user is a home gardener or hobbyist who grows plants for fun in small spaces like balconies, terraces, or backyard gardens and suggest bio pesticide. They are not commercial farmers.
        The plant is affected by the disease: '{disease}'.
        The current weather condition is: '{weather_details}'.
        - Provide the remedies directly without any additional questions and explanation.
        """

        model = genai.GenerativeModel("models/gemini-2.0-flash")
        response = model.generate_content(prompt)

        output = {
            "disease": disease,
            "remedy": response.text.strip()
        }
        return json.dumps(output, indent=2)
    
    except Exception as e:
        error_output = {
            "disease": disease,
            "remedy": f"Error: {str(e)}"
        }
        return json.dumps(error_output, indent=2)

print(get_remedy_for_disease("rust", "Lat: 10.686766287938466, Lon: 78.61553956690796, temperature 28.5 C, weather is Overcast, at 2025-05-02T01:05:33.752456"))
