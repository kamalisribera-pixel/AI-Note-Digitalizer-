from pathlib import Path
from typing import Optional

import cv2
import numpy as np


class ImageLoader:
    SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"]

    def __init__(self):
        self.image = None
        self.path = None

    def load_image(self, image_path: str | Path) -> np.ndarray:
        """
        Function Role: 
            - Load an image from the disk. 
        Arguments:
            - image_path (str | Path): The path to the image file.
        Returns:
            - np.ndarray: The loaded image as a NumPy array.
        Raises:
            - ValueError: If the file extension is not supported.
            - FileNotFoundError: If the image file does not exist.
        """

        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(f"The image file '{image_path}' does not exist.")

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file extension for image '{image_path}'. Supported extensions are: {', '.join(self.SUPPORTED_EXTENSIONS)}")

        image = cv2.imread(str(path))
        self.path = path

        if image is None:
            raise ValueError(f"Failed to load image '{image_path}'.")

        self.image = image
        self.path = path
        return image

    # HELPER PROPERTIES
    @property
    def width(self):
        return self.image.shape[1]

    @property
    def height(self):
        return self.image.shape[0]  

    @property
    def channels(self):
        return self.image.shape[2] 

    @property
    def shape(self):
        return self.image.shape

    @property
    def metadata(self):
        return {
            "path": str(self.path),
            "filename": self.path.name,
            "extension": self.path.suffix,
            "width": self.width,
            "height": self.height,
            "channels": self.channels,
            "shape": self.shape
        }