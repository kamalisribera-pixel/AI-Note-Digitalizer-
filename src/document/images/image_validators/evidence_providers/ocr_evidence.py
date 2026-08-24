from src.ocr.paddle_engine import PaddleOCREngine


class OCREvidence:

    def __init__(self):

        self.ocr = PaddleOCREngine()


    def evaluate(self, image, image_block):

        x1, y1, x2, y2 = image_block.bbox

        crop = image[
            y1:y2,
            x1:x2
        ]


        result = self.ocr.extract_text(
            crop
        )


        score = 0.0


        if result:
            score += 0.5


        if len(result) > 1:
            score += 0.3


        if len(str(result)) > 10:
            score += 0.2


        return {
            "source": "ocr",
            "type": "table",
            "score": min(score, 1.0)
        }