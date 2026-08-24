import cv2

from src.document.images.image_block import ImageBlock
from src.document.images.image_validators.evidence_providers.shape_evidence import ShapeEvidence


image = cv2.imread(
    "tests/images/grid/simple.png"
)


block = ImageBlock(
    bbox=(47,34,182,123),
    image_type="table",
    confidence=0.608
)


provider = ShapeEvidence()

result = provider.evaluate(
    image,
    block
)


print("SHAPE EVIDENCE RESULT")
print(result)