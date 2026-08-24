import cv2

from src.document.images.image_detector import ImageDetector
from src.document.images.image_classifier import ImageClassifier


image = cv2.imread(
    "tests/images/grid/simple.png"
)


detector = ImageDetector()

blocks = detector.detect(image)


classifier = ImageClassifier()


print("IMAGE CLASSIFIER RESULT")


for block in blocks:

    result = classifier.classify(
        block,
        image
    )

    print(result)