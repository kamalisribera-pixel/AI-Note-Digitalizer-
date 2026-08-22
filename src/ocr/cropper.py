from PIL import Image


class ImageCropper:

    def crop(self, image, bounding_box, padding=10):

        x1, y1, x2, y2 = bounding_box

        width, height = image.size

        x1 = max(0, x1 - padding)
        y1 = max(0, y1 - padding)

        x2 = min(width, x2 + padding)
        y2 = min(height, y2 + padding)

        """
        crop = crop.resize(
            (crop.width * 2, crop.height * 2)
        )
        """

        return image.crop(
            (x1, y1, x2, y2)
        )