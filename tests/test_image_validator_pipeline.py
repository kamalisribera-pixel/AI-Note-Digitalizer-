import cv2

from src.document.images.image_block import ImageBlock

from src.document.images.image_validators.image_validators import ImageValidator
from src.document.images.image_validators.decision_engine import DecisionEngine

from src.document.images.image_validators.evidence_providers.vision_evidence import VisionEvidence
from src.document.images.image_validators.evidence_providers.geometry_evidence import GeometryEvidence
from src.document.images.image_validators.evidence_providers.ocr_evidence import OCREvidence
from src.document.images.image_validators.evidence_providers.shape_evidence import ShapeEvidence
from src.document.images.image_validators.evidence_providers.layout_evidence import LayoutEvidence


image = cv2.imread(
    "tests/images/grid/simple.png"
)


block = ImageBlock(
    bbox=(47, 34, 182, 123),
    image_type="unknown",
    confidence=1.0
)


validator = ImageValidator(
    VisionEvidence(),
    GeometryEvidence(),
    OCREvidence(),
    ShapeEvidence(),
    LayoutEvidence(),
    DecisionEngine()
)


result = validator.validate(
    image,
    block
)


print("FINAL IMAGE VALIDATION RESULT")
print(result)

print("\nMETADATA")
print(result.metadata)