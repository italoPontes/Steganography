"""
Utils.py

This module provides utility functions for image processing.

"""
import numpy as np
from PIL import Image


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
