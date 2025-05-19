import openai
import os
from openai import OpenAI
import urllib.request
from dotenv import load_dotenv
import streamlit as st
import base64
from io import BytesIO
from PIL import Image
import time

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def generate_image_openai(prompt):
    response = client.images.generate(
        model="gpt-image-1",  # Nouveau modèle
        prompt=prompt,
        size="1024x1024",
        n=1,
    )
    # Récupérer l'image en base64
    image_data = response.data[0].b64_json
    
    # Créer un répertoire pour stocker les images si nécessaire
    os.makedirs("static/generated_images", exist_ok=True)
    
    # Générer un nom de fichier unique
    filename = f"static/generated_images/image_{int(time.time())}.png"
    
    # Convertir base64 en image et sauvegarder
    img = Image.open(BytesIO(base64.b64decode(image_data)))
    img.save(filename)
    
    # Retourner le chemin du fichier local
    return filename

def save_img(img_url, file_path):
    urllib.request.urlretrieve(img_url, file_path)
