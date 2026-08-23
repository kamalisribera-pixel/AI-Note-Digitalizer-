import cv2
import numpy as np


class HorizontalLine:
    def __init__(self, x1, y, x2, confidence=1.0):
        self.x1 = x1
        self.y = y
        self.x2 = x2
        self.confidence = confidence

    def __repr__(self):
        return (
            f"HorizontalLine("
            f"x1={self.x1}, y={self.y}, "
            f"x2={self.x2}, "
            f"confidence={self.confidence})"
        )


def detect_horizontal_lines(binary_image):

    height, width = binary_image.shape

    # Kernel length controls minimum detectable line length
    kernel_length = max(10, width // 20)

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (kernel_length, 1)
    )

    # Extract horizontal lines
    horizontal = cv2.morphologyEx(
        binary_image,
        cv2.MORPH_OPEN,
        kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        horizontal,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    lines = []

    for contour in contours:

        x, y, w, h = cv2.boundingRect(contour)

        # Ignore tiny noise
        if w < kernel_length:
            continue

        line = HorizontalLine(
            x1=x,
            y=y + h // 2,
            x2=x + w
        )

        lines.append(line)

    # Sort from top to bottom
    lines.sort(key=lambda line: line.y)

    return lines

def draw_horizontal_lines(image, lines):

    output = image.copy()

    for line in lines:
        cv2.line(
            output,
            (line.x1, line.y),
            (line.x2, line.y),
            (0, 0, 255),
            2
        )

    return output