from PIL import Image

from src.ocr.paddle_engine import PaddleOCREngine
from src.ocr.trocr_engine import TrOCREngine


class OCRPipeline:

    CONFIDENCE_THRESHOLD = 0.95


    def __init__(self):
        self.paddle = PaddleOCREngine()
        self.trocr = TrOCREngine()


    def crop_region(self, image, bounding_box):

        x1, y1, x2, y2 = bounding_box

        crop = image.crop(
            (x1, y1, x2, y2)
        )

        return crop


    def extract_text(self, image_path):

        image = Image.open(image_path).convert("RGB")

        paddle_results = self.paddle.extract_text(
            image_path
        )

        final_results = []


        for item in paddle_results:

            if item["confidence"] >= self.CONFIDENCE_THRESHOLD:

                final_results.append(
                    item["text"]
                )


            else:

                crop = self.crop_region(
                    image,
                    item["bounding_box"]
                )


                trocr_text = self.trocr.extract_text(
                    crop
                )


                final_results.append(
                    trocr_text
                )


        return final_results