from pymongo import MongoClient
from urllib.parse import quote_plus
import os
import streamlit as st

def init_connection():
    username = quote_plus(st.secrets["mongo"]["username"])
    password = quote_plus(st.secrets["mongo"]["password"])
    uri = f"mongodb+srv://{username}:{password}@cluster0.q3crdzn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    return client
