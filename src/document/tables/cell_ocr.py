from PIL import Image
import cv2

from src.ocr.ocr_engine import OCREngine


class CellOCR:

    def __init__(self):
        self.ocr = OCREngine()


    def extract_text(self, cells):

        results = []

        for item in cells:

            cell = item["cell"]
            crop = item["image"]

            # OpenCV BGR → RGB → PIL
            rgb = cv2.cvtColor(
                crop,
                cv2.COLOR_BGR2RGB
            )

            pil_image = Image.fromarray(rgb)

            text = self.ocr.recognize_text(
                pil_image
            )

            results.append(
                {
                    "cell": cell,
                    "text": text
                }
            )

        return results