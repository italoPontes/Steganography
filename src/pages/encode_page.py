"""
Docstring
"""
import cv2
import streamlit as st
import numpy as np
import utils
from steganography import Steganography

output_file_name = "encoded_image.png"
encode_diagram_file_name = "../data/encode_diagram.png"

model = Steganography()

st.title("Steganography Demo")

st.markdown("Breve texto 2")

st.image(encode_diagram_file_name)

base_image_name = st.file_uploader("Choose the Base Image",
                                   accept_multiple_files = False)

cover_image_name = st.file_uploader("Choose the Cover Image",
                                    accept_multiple_files = False)

if (base_image_name is not None) and (cover_image_name is not None):
    with st.spinner("Running... Please, wait a few seconds."):
        embedded_image = utils.load_image(cover_image_name)
        hidden_image = utils.load_image(base_image_name)

        encoded_image = model.encode(embedded_image, hidden_image)
        encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(output_file_name, encoded_image)

        with open(output_file_name, "rb") as file:
            btn = st.download_button(label = "Download image",
                                    data = file,
                                    file_name = output_file_name,
                                    mime = "image/png")
