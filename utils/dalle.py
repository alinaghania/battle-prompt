import openai
import streamlit as st
import urllib.request

# Access the API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

def generate_image_openai(prompt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def save_img(img_url, file_path):
    urllib.request.urlretrieve(img_url, file_path)
