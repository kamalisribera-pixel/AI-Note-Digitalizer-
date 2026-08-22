import cv2
import numpy as np
def deskew_image(image: np.ndarray) -> np.ndarray:
    coordinates = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coordinates)[-1]
    if angle < -45:
        angle = (90 + angle)

    rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), angle, 1)
    deskewed_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return deskewed_image