from .document_block import DocumentBlock


def create_document_blocks(text_blocks):
    document_blocks = []

    for block in text_blocks:
        x1, y1, x2, y2 = block.bounding_box

        document_block = DocumentBlock(
            text=block.text,
            bbox=block.bounding_box,
            confidence=block.confidence
        )

        # Basic geometry
        document_block.width = x2 - x1
        document_block.height = y2 - y1

        # Basic text features
        document_block.word_count = len(block.text.split())
        document_block.char_count = len(block.text)

        if document_block.char_count > 0:
            uppercase = sum(
                1 for c in block.text if c.isupper()
            )

            document_block.uppercase_ratio = (
                uppercase / document_block.char_count
            )

        document_blocks.append(document_block)

    return document_blocks