import cv2

from src.document.tables.grid.horizontal_detector import (
    detect_horizontal_lines,
    draw_horizontal_lines
)

from src.document.tables.grid.preprocess import preprocess_table


image = cv2.imread("tests/images/grid/simple.png")

# preprocessing
binary = preprocess_table(image)

cv2.imshow("Binary", binary)
cv2.waitKey(0)


# detect horizontal lines
lines = detect_horizontal_lines(binary)

print("Detected lines:", len(lines))
print(lines)


# draw on original image
result = draw_horizontal_lines(
    image,
    lines
)

cv2.imshow(
    "Horizontal Lines",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()