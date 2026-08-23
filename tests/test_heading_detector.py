from src.layout.document_block import DocumentBlock
from src.document.heading.heading_detector import detect_headings


blocks = [
    DocumentBlock(
        text="INTRODUCTION",
        bbox=[300,50,500,90],
        height=40,
        word_count=1,
        uppercase_ratio=1.0,
        gap_below=60,
        center_offset=0
    ),

    DocumentBlock(
        text="Neural networks are computational models",
        bbox=[100,150,600,190],
        height=40,
        word_count=5,
        uppercase_ratio=0.025,
        gap_above=60,
        center_offset=50
    ),

    DocumentBlock(
        text="CHAPTER 3",
        bbox=[300,50,500,90],
        height=40,
        width=200,
        width_ratio=0.25,
        word_count=2,
        uppercase_ratio=1.0,
        has_numbering=True,
        gap_below=30,
        center_offset=0
    )
]


blocks = detect_headings(blocks)


for block in blocks:
    print(block.text, "→", block.block_type)