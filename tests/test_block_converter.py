from src.layout.text_block import TextBlock
from src.layout.block_converter import create_document_blocks


ocr_blocks = [
    TextBlock(
        text="INTRODUCTION",
        bounding_box=[100, 50, 300, 90],
        confidence=0.98
    ),

    TextBlock(
        text="Neural networks are computational models",
        bounding_box=[100, 120, 600, 160],
        confidence=0.95
    )
]


blocks = create_document_blocks(ocr_blocks)


for block in blocks:
    print(block)