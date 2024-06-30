# import openai
# import os
# from openai import OpenAI
# import urllib.request
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# client = st.secrets["openai"]["api_key"]

# def generate_image_openai(prompt):
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )

#     image_url = response.data[0].url
#     return image_url

import openai
import urllib.request
import streamlit as st

# Access the API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

def generate_image_openai(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def save_img(img_url, file_path):
    urllib.request.urlretrieve(img_url, file_path)


# def save_img(img_url, file_path):
#     urllib.request.urlretrieve(img_url, file_path)