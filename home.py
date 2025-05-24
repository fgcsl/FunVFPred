# Home.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Bioinformatics Tool", layout="centered")
st.title("Welcome to the AAC Bioinformatics Tool")
st.image("logo.png", width=300)
st.write("""
This web application allows you to extract Amino Acid Composition (AAC) features from protein sequences in FASTA format and merge them with label data.  
Navigate to **Predict** to start processing your data.
""")
