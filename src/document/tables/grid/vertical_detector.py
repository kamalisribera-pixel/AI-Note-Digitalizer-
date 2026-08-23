import cv2


class VerticalLine:
    def __init__(self, x, y1, y2, confidence=1.0):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.confidence = confidence

    def __repr__(self):
        return (
            f"VerticalLine("
            f"x={self.x}, "
            f"y1={self.y1}, "
            f"y2={self.y2}, "
            f"confidence={self.confidence})"
        )


def detect_vertical_lines(binary_image):

    height, width = binary_image.shape

    kernel_length = max(10, height // 20)

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (1, kernel_length)
    )

    vertical = cv2.morphologyEx(
        binary_image,
        cv2.MORPH_OPEN,
        kernel
    )

    contours, _ = cv2.findContours(
        vertical,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    lines = []

    for contour in contours:

        x, y, w, h = cv2.boundingRect(contour)

        if h < kernel_length:
            continue

        line = VerticalLine(
            x=x + w // 2,
            y1=y,
            y2=y + h
        )

        lines.append(line)

    lines.sort(key=lambda line: line.x)

    return lines


def draw_vertical_lines(image, lines):

    output = image.copy()

    for line in lines:
        cv2.line(
            output,
            (line.x, line.y1),
            (line.x, line.y2),
            (255, 0, 0),
            2
        )

    return output