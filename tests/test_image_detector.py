import cv2
from src.document.images.image_detector import ImageDetector

image = cv2.imread(
    "tests/images/grid/simple.png"
)


detector = ImageDetector()

results = detector.detect(image)


print("IMAGE DETECTOR RESULT")

print(
    "Total images:",
    len(results)
)


for img in results:
    print(img)