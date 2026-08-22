import numpy as np

def normalize_image(image: np.ndarray) -> np.ndarray:
    image_array = np.array(image)
    if not isinstance(image_array, np.ndarray):
        raise ValueError("Input must be a NumPy array representing an image.")

    # Normalize the image to the range [0, 1]
    normalized_image = image_array.astype(np.float32) / 255.0
    return normalized_image