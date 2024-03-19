"""
Steganography Demo

This module provides a Streamlit web application for demonstrating
steganography techniques.

"""
import cv2
import streamlit as st
import utils
from steganography import Steganography

utils.get_credentials()

OUTPUT_FILE_NAME = "data/encoded_image.png"
ENCODE_DIAGRAM_FILE_NAME = "data/Diagrams/encode_diagram.png"

model = Steganography()

st.title("Steganography Demo")
st.image(ENCODE_DIAGRAM_FILE_NAME)

base_image_name = st.file_uploader("Choose the Base Image",
                                   accept_multiple_files=False)

cover_image_name = st.file_uploader("Choose the Cover Image",
                                    accept_multiple_files=False)

if (base_image_name is not None) and (cover_image_name is not None):
    with st.spinner("Running... Please, wait a few seconds."):
        embedded_image = utils.load_image(cover_image_name)
        hidden_image = utils.load_image(base_image_name)

        encoded_image = model.encode(embedded_image, hidden_image)
        encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(OUTPUT_FILE_NAME, encoded_image)

        with open(OUTPUT_FILE_NAME, "rb") as file:
            btn = st.download_button(label="Download image",
                                     data=file,
                                     file_name=OUTPUT_FILE_NAME,
                                     mime="image/png")
