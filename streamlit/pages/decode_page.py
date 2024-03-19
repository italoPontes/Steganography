"""
Steganography Demo

This module provides a Streamlit web application for
decoding steganography images.

"""
import streamlit as st
import utils
from steganography import Steganography

utils.get_credentials()

OUTPUT_FILE_NAME = "decode_image.png"
DECODE_DIAGRAM_FILE_NAME = "data/Diagrams/decode_diagram.png"

model = Steganography()

st.title("Steganography Demo")
st.image(DECODE_DIAGRAM_FILE_NAME)

encoded_image_name = st.file_uploader("Choose the Steganography Image",
                                      accept_multiple_files=False)

if encoded_image_name is not None:
    with st.spinner("Running... Please, wait a few seconds."):
        encoded_image = utils.load_image(encoded_image_name)
        retrieved_image = model.decode(encoded_image)

        st.markdown("Decoded image:")
        st.image(retrieved_image)
