import cv2

from src.document.images.image_detector import ImageDetector
from src.document.images.image_classifier import ImageClassifier
from src.document.images.image_validator import ImageValidator


image = cv2.imread(
    "tests/images/grid/simple.png"
)

detector = ImageDetector()
classifier = ImageClassifier()
validator = ImageValidator()

blocks = detector.detect(image)

print("IMAGE VALIDATOR RESULT")

for block in blocks:

    block = classifier.classify(block, image)

    print("Before:", block)

    block = validator.validate(image, block)

    print("After :", block)