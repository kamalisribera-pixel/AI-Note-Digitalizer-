from src.layout.document_block import DocumentBlock
from src.document.heading.heading_features import calculate_heading_features


blocks = [
    DocumentBlock(
        text="CHAPTER 3",
        bbox=[300, 50, 500, 90],
        width=200,
        height=40
    ),

    DocumentBlock(
        text="INTRODUCTION",
        bbox=[300, 120, 500, 160],
        width=200,
        height=40
    ),

    DocumentBlock(
        text="Neural networks are computational models",
        bbox=[100, 220, 600, 260],
        width=500,
        height=40
    )
]

blocks = calculate_heading_features(
    blocks,
    page_width=800
)


for block in blocks:
    print(block.text)
    print("Gap above:", block.gap_above)
    print("Gap below:", block.gap_below)
    print("Center offset:", block.center_offset)
    print("Has numbering:", block.has_numbering)
    print("Numbering type:", block.numbering_type)
    print("----------------")