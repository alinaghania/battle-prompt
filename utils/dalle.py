import openai
import os
from openai import OpenAI
import urllib.request
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image_openai(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return image_url

def save_img(img_url, file_path):
    urllib.request.urlretrieve(img_url, file_path)
