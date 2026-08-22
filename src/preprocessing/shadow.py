import cv2
import numpy as np

def remove_shadows(image: np.ndarray) -> np.ndarray:
    background = cv2.GaussianBlur(image, (51, 51), 0)
    shadowless_image = cv2.divide(image, background, scale=255)
    return shadowless_image