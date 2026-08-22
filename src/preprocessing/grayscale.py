import cv2
import numpy as np

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.array(gray_image)