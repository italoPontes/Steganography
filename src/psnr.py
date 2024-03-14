"""
This module provides a class to calculate the
Peak Signal-to-Noise Ratio (PSNR) for comparing the
quality of two images.
"""
import numpy as np


def compute_mean_squared_error(image_src: np.ndarray,
                               image_ref: np.ndarray) -> float:
    """
    Computes the mean squared error between two images.

    Args:
        image_src (numpy.ndarray): Source image.
        image_ref (numpy.ndarray): Reference image.

    Returns:
        float: The mean squared error between the two images,
        or -inf if the images have different shapes.
    """
    # Check if the images have the same shape
    if image_src.shape != image_ref.shape:
        return float('-inf')

    # Compute the mean squared error
    mse = np.mean((image_src - image_ref) ** 2)
    return mse


def compute_psnr(image_src: np.ndarray, image_ref: np.ndarray) -> float:
    """
    Computes the Peak Signal-to-Noise Ratio (PSNR) between two images.

    Args:
        image_src (numpy.ndarray): Source image.
        image_ref (numpy.ndarray): Reference image.

    Returns:
        float: The PSNR value between the two images,
        or -inf if the images have different shapes.
    """
    # Check if the images have the same shape
    if image_src.shape != image_ref.shape:
        return float('-inf')

    # Compute the mean squared error between the images
    mse = compute_mean_squared_error(image_src, image_ref)

    # Compute the range of pixel values in the source image
    pixel_range = np.max(image_src) - np.min(image_src)

    if pixel_range == 0:
        return float('-inf')

    # Compute the PSNR value
    psnr = 10 * np.log10((pixel_range ** 2) / mse)

    return psnr
