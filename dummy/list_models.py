import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="AIzaSyCPISwKHCyjN0UUVHUmyPC-YhCbEh19hzg")

# Get the models and print them
models = list(genai.list_models())  # Convert the generator to a list
print(models)
