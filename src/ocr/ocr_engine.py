from paddleocr import PaddleOCR
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

class OCREngine:
    def __init__(self):
        self.paddle = PaddleOCR(lang="en", use_doc_orientation_classify=False, use_doc_unwarping=False, use_textline_orientation=False)

        self.processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten", use_fast = False)
        self.model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
        self.model.eval()

    def detect_text_regions(self, image_path):
        result = self.paddle.predict(image_path)
        return result
    def recognize_text(self,crop):
        pixel_values = self.processor(images=crop, return_tensors="pt").pixel_values

        with torch.no_grad():
            generated_ids = self.model.generate(pixel_values, max_new_tokens = 64)

        text = self.processor.batch_decode(generated_ids, skip_special_tokens = True)[0]

        return text
    def extract_text(self, image_path):
        regions = self.detect_text_regions(image_path)
        return regions