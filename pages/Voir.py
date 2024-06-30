import streamlit as st
from utils.db_manager import init_connection

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

st.title("Liste des prompts")

# Menu to select the round
round_choice = st.selectbox("Choisissez la manche", ["Manche 1", "Manche 2", "Manche 3", "Manche 4"])
round_mapping = {"Manche 1": 1, "Manche 2": 2, "Manche 3": 3, "Manche 4": 4}
selected_round = round_mapping[round_choice]

prompts = prompts_collection.find({"round": selected_round}, {"_id": 0, "username": 1, "prompt": 1, "image_url": 1})
for prompt in prompts:
    st.write(f"{prompt.get('username', 'Anonyme')} : {prompt['prompt']}")
    if "image_url" in prompt and prompt["image_url"]:
        st.image(prompt["image_url"], width=300)
