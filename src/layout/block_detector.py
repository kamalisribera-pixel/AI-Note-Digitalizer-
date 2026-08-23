from .text_block import TextBlock

def detect_blocks(ocr_results):
    blocks = []
    heights = []

    for item in ocr_results:
        bbox = item["bbox"]

        height = bbox[3] -bbox[1]
        heights.append(height)

    average_height = sum(heights) / len(heights)

    for item in ocr_results:
        bbox = item["bbox"]
        height = bbox[3] -bbox[1]

        if height >= average_height * 1.5:
            block_type = "heading"
        else:
            block_type = "paragraph"
        block = DocumentBlock(
            text=item["text"],
            block_type=block_type,
            bbox=bbox,
            confidence=item.get(
                "confidence",
                1.0
            )
        )

        blocks.append(block)


    return blocks