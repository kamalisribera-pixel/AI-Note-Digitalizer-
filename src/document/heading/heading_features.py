
import re
def calculate_heading_features(blocks, page_width):
    # Sort blocks from top to bottom
    blocks = sorted(
        blocks,
        key=lambda block: block.bbox[1]
    )
    
    for i, block in enumerate(blocks):

        x1, y1, x2, y2 = block.bbox

        # Center alignment feature
        block_center = (x1 + x2) / 2
        page_center = page_width / 2

        block.center_offset = abs(
            block_center - page_center
        )

        # Vertical spacing features
        if i > 0:
            previous = blocks[i - 1]

            _, prev_y1, _, prev_y2 = previous.bbox

            block.gap_above = y1 - prev_y2

        if i < len(blocks) - 1:
            next_block = blocks[i + 1]

            _, next_y1, _, _ = next_block.bbox

            block.gap_below = next_y1 - y2

        block.width_ratio = block.width / page_width

        block.has_numbering = detect_numbering(
            block.text
        )

    return blocks
def detect_numbering(text):
    patterns = [
        r"^\d+\.",
        r"^\d+\.\d+",
        r"^chapter\s+\d+",
        r"^section\s+\d+",
        r"^[IVXLCDM]+\.",
        r"^[A-Z]\."
    ]

    for pattern in patterns:
        if re.match(pattern, text, re.IGNORECASE):
            return True

    return False