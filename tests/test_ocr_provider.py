import cv2

from src.document.images.image_block import ImageBlock
from src.document.images.image_validators.evidence_providers.ocr_evidence import OCREvidence


image = cv2.imread(
    "tests/images/grid/simple.png"
)


block = ImageBlock(
    bbox=(47, 34, 182, 123),
    image_type="table",
    confidence=0.608
)


evidence = OCREvidence()


result = evidence.evaluate(
    image,
    block
)


print("OCR EVIDENCE RESULT")
print(result)