import os

os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"


from paddleocr import PaddleOCR

class PaddleOCREngine:
    def __init__(self):
        self.model = PaddleOCR(lang='en', enable_mkldnn=False)
    def extract_text(self, image):
        result = self.model.predict(image)
        return result