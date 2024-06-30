import streamlit as st
from utils.db_manager import init_connection
from utils.dalle import generate_image_openai

# Initialize connection
client = init_connection()
db = client['prompt_battle']
prompts_collection = db['prompts']

# Ensure pseudonym is entered
if 'username' not in st.session_state:
    pseudonym = st.text_input("Entrez votre pseudonyme pour continuer")
    if pseudonym:
        st.session_state['username'] = pseudonym.capitalize()
    else:
        st.stop()

username = st.session_state['username']

st.title(f"Ajouter un prompt pour Manche 3, {username}")
st.image('static/assets/manche3.webp', width=600)
prompt = st.text_area(f"Essaie de reproduire cette image, {username}")

if st.button("Ajouter"):
    if prompt:
        image_url = generate_image_openai(prompt)
        prompts_collection.insert_one({"username": username, "prompt": prompt, "image_url": image_url, "round": 3})
        st.success("Prompt ajouté avec succès!")
        st.image(image_url, width=300)
    else:
        st.error("Veuillez entrer un prompt.")
