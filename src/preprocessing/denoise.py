import cv2
import numpy as np

from src.preprocessing.config import MEDIAN_KERNEL_SIZE


def denoise_image(image: np.ndarray) -> np.ndarray:
    denoised_image = cv2.medianBlur(image, MEDIAN_KERNEL_SIZE)

    return denoised_image