import cv2

from src.document.images.image_block import ImageBlock
from src.document.images.image_validators.evidence_providers.geometry_evidence import GeometryEvidence


image = cv2.imread(
    "tests/images/grid/simple.png"
)


block = ImageBlock(
    bbox=(47, 34, 182, 123),
    image_type="table",
    confidence=0.608
)


evidence = GeometryEvidence()


result = evidence.evaluate(
    image,
    block
)


print("GEOMETRY EVIDENCE RESULT")
print(result)