import cv2
import numpy as np

from src.preprocessing.config import CLAHE_CLIP_LIMIT, CLAHE_TILE_GRID_SIZE

def enhance_contrast(image: np.ndarray) -> np.ndarray:
    clahe = cv2.createCLAHE(clipLimit=CLAHE_CLIP_LIMIT, tileGridSize=CLAHE_TILE_GRID_SIZE)
    contrasted_image = clahe.apply(image)
    return contrasted_image
