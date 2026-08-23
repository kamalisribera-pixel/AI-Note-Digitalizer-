import cv2

from .image_block import ImageBlock


class ImageDetector:

    def detect(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        # find non-white regions
        threshold = cv2.threshold(
            gray,
            240,
            255,
            cv2.THRESH_BINARY_INV
        )[1]

        contours, _ = cv2.findContours(
            threshold,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        images = []

        for contour in contours:

            x, y, w, h = cv2.boundingRect(contour)

            area = w * h

            # ignore small text-like regions
            if area < 10000:
                continue

            images.append(
                ImageBlock(
                    bbox=(
                        x,
                        y,
                        x + w,
                        y + h
                    )
                )
            )

        return images