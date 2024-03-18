"""
Utils.py

This module provides utility functions for image processing.

"""
import streamlit as st
import numpy as np
from PIL import Image
import base64


def load_image(image_object) -> np.ndarray:
    """
    Load an image from the given image object.

    Parameters:
    - image_object: A file-like object representing the image.

    Returns:
    - An array representation of the loaded image.

    """
    image = Image.open(image_object)
    image = np.array(image)
    return image

def get_credentials():
    """
    Display personal credentials in the Streamlit sidebar.

    This function displays personal credentials, including
    a photo, name, and links to LinkedIn and GitHub,
    in the Streamlit sidebar.
    """
    linkedin_photo = "data/logos/Linkedin-logo.png"
    github_photo = "data/logos/Github-logo.png"
    personal_photo = "data/Italo.jpeg"
    github = "github.com/italoPontes/Steganography"
    github_url = "https://github.com/italoPontes/Steganography/"

    st.sidebar.markdown(
        """<a href="https://www.linkedin.com/in/italo-de-pontes/">
        <img src="data:image/png;base64,{}" width="100">
        </a>""".format(
            base64.b64encode(open(linkedin_photo, "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("")
    st.sidebar.image(personal_photo)
    st.sidebar.markdown("Developed by:")
    st.sidebar.markdown("Ítalo de Pontes Oliveira")
    st.sidebar.markdown(
        """<a href="https://github.com/italoPontes/Steganography/">
        <img src="data:image/png;base64,{}" width="100">
        </a>""".format(
            base64.b64encode(open(github_photo, "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
    st.sidebar.write(f"[{github}]({github_url})")
    st.sidebar.markdown("")
