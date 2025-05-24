# Predict.py
import streamlit as st
import os
import uuid
import pandas as pd
from logic.extract_features import extract_features

st.title("AAC Feature Prediction")

fasta_file = st.file_uploader("Upload FASTA File", type=["fasta"])
label_file = st.file_uploader("Upload Label File (CSV)", type=["csv"])

if fasta_file and label_file:
    user_id = str(uuid.uuid4())
    os.makedirs(f"FILES/{user_id}", exist_ok=True)

    fasta_path = f"FILES/{user_id}/uploaded.fasta"
    label_path = f"FILES/{user_id}/uploaded.csv"
    output_path = f"FILES/{user_id}/AAC.csv"

    # Save uploaded files
    with open(fasta_path, "wb") as f:
        f.write(fasta_file.read())
    with open(label_path, "wb") as f:
        f.write(label_file.read())

    # Run feature extraction
    features_df = extract_features(fasta_path, label_path)
    features_df.to_csv(output_path, index=False)

    st.success("Feature extraction complete.")
    st.download_button("Download AAC.csv", data=open(output_path, "rb"), file_name="AAC.csv")
