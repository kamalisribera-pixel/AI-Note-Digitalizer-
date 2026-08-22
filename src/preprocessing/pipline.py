from src.preprocessing.image_loader import ImageLoader
from src.preprocessing.grayscale import convert_to_grayscale
from src.preprocessing.shadow import remove_shadows
from src.preprocessing.denoise import denoise_image
from src.preprocessing.resize import resize_image
from src.preprocessing.contrast import enhance_contrast
from src.preprocessing.sharpen import sharpen_image
from src.preprocessing.threshold import apply_threshold
from src.preprocessing.morphology import opening, closing
from src.preprocessing.deskew import deskew_image
from src.preprocessing.tensor import image_to_tensor
from src.preprocessing.normalize import normalize_image

from src.preprocessing.config import IMAGE_SIZE

import numpy as np

class PreprocessingPipeline:
    def __init__(self):
        self.loader = ImageLoader()

    def process(self, image_path: str) -> np.ndarray:
        image = self.loader.load_image(image_path)
        image = convert_to_grayscale(image)
        image = remove_shadows(image)
        image = denoise_image(image)
        image = enhance_contrast(image)
        image = sharpen_image(image)
        image = apply_threshold(image)
        image = opening(image)
        image = closing(image)
        image = deskew_image(image)
        image = resize_image(image, IMAGE_SIZE)
        image = normalize_image(image)
        image = image_to_tensor(image)

        return image