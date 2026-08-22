import cv2
import numpy as np

def resize_image(image: np.ndarray, size: tuple[int, int]) -> np.ndarray:
    resized_image = cv2.resize(image, size, interpolation=cv2.INTER_LANCZOS4)
    return resized_image