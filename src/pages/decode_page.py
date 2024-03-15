"""
Docstring
"""
import cv2
import streamlit as st
import utils
from steganography import Steganography

output_file_name = "decode_image.png"
encode_diagram_file_name = "../data/decode_diagram.png"

model = Steganography()

st.title("Steganography Demo")

st.image(encode_diagram_file_name)

encoded_image_name = st.file_uploader("Choose the Steganography Image",
                                       accept_multiple_files = False)

if (encoded_image_name is not None):
    with st.spinner("Running... Please, wait a few seconds."):
        encoded_image = utils.load_image(encoded_image_name)

        '''
        retrieved_image = model.decode(encoded_image)
        retrieved_image = cv2.cvtColor(retrieved_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(output_file_name, retrieved_image)

        with open(output_file_name, "rb") as file:
            btn = st.download_button(label = "Download image",
                                    data = file,
                                    file_name = output_file_name,
                                    mime = "image/png")
        '''