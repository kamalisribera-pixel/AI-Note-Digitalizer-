import cv2
import numpy as np

from src.preprocessing.deskew import deskew_image
from src.preprocessing.grayscale import convert_to_grayscale
from src.preprocessing.denoise import denoise_image
from src.preprocessing.image_loader import ImageLoader
from src.preprocessing.morphology import closing, opening
from src.preprocessing.morphology import opening
from src.preprocessing.resize import resize_image
from src.preprocessing.contrast import enhance_contrast
from src.preprocessing.sharpen import sharpen_image
from src.preprocessing.threshold import apply_threshold
from src.preprocessing.shadow import remove_shadows

loader = ImageLoader()

image = loader.load_image("data/raw/notes.png")

gray = convert_to_grayscale(image)

shadow_free = remove_shadows(gray)

denoised = denoise_image(shadow_free)

resized = resize_image(denoised, (224, 224))

contrasted = enhance_contrast(resized)

sharpened = sharpen_image(contrasted)

threshold = apply_threshold(sharpened)

cleaned = opening(threshold)

clean = closing(cleaned)

deskewed = deskew_image(threshold)




cv2.imwrite("shadow_removed.jpg", shadow_free)