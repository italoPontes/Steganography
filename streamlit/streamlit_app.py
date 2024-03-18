"""
Docstring
"""
import streamlit as st
import base64 

import sys
sys.path.append("src")
import utils

st.set_page_config(layout="wide")

utils.get_credentials()

ENCODE_FULL_DIAGRAM_FILE_NAME = "data/encode_full_diagram.png"
DECODE_FULL_DIAGRAM_FILE_NAME = "data/decode_full_diagram.png"

st.page_link("streamlit_app.py", label="Home", icon="🏠")

left_column, right_column = st.columns(2)

with left_column:
    st.page_link("pages/encode_page.py", label="Encode Page", icon="1️⃣")
    st.image(ENCODE_FULL_DIAGRAM_FILE_NAME)

with right_column:
    st.page_link("pages/decode_page.py", label="Decode Page", icon="2️⃣")
    st.image(DECODE_FULL_DIAGRAM_FILE_NAME)
