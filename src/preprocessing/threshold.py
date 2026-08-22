import cv2
import numpy as np

from src.preprocessing.config import THRESHOLD_ADAPTIVE_METHOD, THRESHOLD_BLOCK_SIZE, THRESHOLD_C, THRESHOLD_TYPE

from src.preprocessing.config import THRESHOLD_MAX_VALUE

def apply_threshold(image: np.ndarray) -> np.ndarray:
    threshold_image = cv2.adaptiveThreshold(
        image,
        maxValue=THRESHOLD_MAX_VALUE,
        adaptiveMethod=THRESHOLD_ADAPTIVE_METHOD,
        thresholdType=THRESHOLD_TYPE,
        blockSize=THRESHOLD_BLOCK_SIZE,
        C=THRESHOLD_C   
    )

    return threshold_image
