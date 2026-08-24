from src.document.images.image_block import ImageBlock
from src.document.images.image_validators.evidence_providers.vision_evidence import VisionEvidence

block = ImageBlock(
    bbox=(5, 15, 187, 127),
    image_type="table",
    confidence=0.608
)


evidence = VisionEvidence()


result = evidence.evaluate(block)


print("VISION EVIDENCE RESULT")
print(result)