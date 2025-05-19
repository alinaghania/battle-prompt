import openai
import os
from openai import OpenAI
import urllib.request
from dotenv import load_dotenv
import streamlit as st

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def generate_image_openai(prompt):
    response = client.images.generate(
        model="gpt-image-1",  # Nouveau modèle
        prompt=prompt,
        size="1024x1024",
        n=1,
    )
    # Avec gpt-image-1, la réponse contient toujours une image encodée en base64
    # et non une URL comme avec dall-e-3
    image_data = response.data[0].b64_json
    # Vous devrez adapter le code pour traiter l'image en base64 au lieu d'une URL
    return image_data

def save_img(img_url, file_path):
    urllib.request.urlretrieve(img_url, file_path)
