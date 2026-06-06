import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carga tu clave
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Solo imprime los nombres de los modelos disponibles
print("Modelos disponibles:")
for m in genai.list_models():
    print(m.name)