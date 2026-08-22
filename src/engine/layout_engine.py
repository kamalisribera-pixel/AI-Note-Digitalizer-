from src.layout.reading_order import sort_reading_order
from layout.block_detector import detect_blocks


class LayoutEngine:

    def __init__(self):
        pass


    def analyze(self, ocr_results):

        # Step 1: arrange text in reading order
        ordered_text = sort_reading_order(
            ocr_results
        )


        # Step 2: detect document blocks
        blocks = detect_blocks(
            ordered_text
        )


        return blocks