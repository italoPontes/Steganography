"""
Utils.py

"""
import numpy as np
from PIL import Image

def load_image(image_name: str = "") -> np.ndarray:
    """
        Docstring
    """
    image = Image.open(image_name.name)
    image = np.array(image)
    return image