import cv2
import numpy as np

def erode(image: np.ndarray, kernel_size: tuple[int,int]=(3,3), iterations: int = 1) -> np.ndarray:
    kernel = np.ones(kernel_size, dtype=np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=iterations)
    return eroded_image

def dilate(image: np.ndarray, kernel_size: tuple[int,int]=(3,3), iterations: int = 1) -> np.ndarray:
    kernel = np.ones(kernel_size, dtype=np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    return dilated_image

def opening(image: np.ndarray, kernel_size: tuple[int,int]=(3,3)) -> np.ndarray:
    kernel = np.ones(kernel_size, dtype=np.uint8)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opened_image

def closing(image: np.ndarray, kernel_size: tuple[int,int]=(3,3)) -> np.ndarray:
    kernel = np.ones(kernel_size, dtype=np.uint8)
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closed_image