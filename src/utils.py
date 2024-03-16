"""
Utils.py

"""
import numpy as np
from PIL import Image

def load_image(image_object) -> np.ndarray:
    """
        Docstring
    """
    image = Image.open(image_object)
    image = np.array(image)
    return image