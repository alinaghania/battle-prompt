import streamlit as st
from utils.db_manager import init_connection
import os

# Initialize connection
client = init_connection()
db = client['prompt_battle']
prompts_collection = db['prompts']

# Page configuration
st.set_page_config(page_title="Accueil")

# Pseudonym input
if 'username' not in st.session_state:
    pseudonym = st.text_input("Entrez votre pseudonyme pour continuer")
    if pseudonym:
        st.session_state['username'] = pseudonym.capitalize()
    else:
        st.stop()

username = st.session_state['username']

st.title(f"Bienvenue à Prompt Battle, {username}")

# Sidebar menu
menu = ["Accueil", "Manche 1", "Manche 2", "Manche 3", "Manche 4", "Voir les prompts"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Accueil":
    st.image('static/assets/example.JPG', width=300)

elif choice == "Manche 1":
    st.experimental_rerun('pages/Manche1.py')

elif choice == "Manche 2":
    st.experimental_rerun('pages/Manche2.py')

elif choice == "Manche 3":
    st.experimental_rerun('pages/Manche3.py')

elif choice == "Manche 4":
    st.experimental_rerun('pages/Manche4.py')

elif choice == "Voir les prompts":
    st.experimental_rerun('pages/Voir.py')
