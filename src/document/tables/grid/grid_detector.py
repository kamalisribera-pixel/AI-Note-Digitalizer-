import cv2


def detect_grid(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        1,
        3.14 / 180,
        threshold=100,
        minLineLength=100,
        maxLineGap=5
    )

    if lines is None:
        return False

    return len(lines) > 10