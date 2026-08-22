from src.ocr.paddle_engine import PaddleOCREngine
from src.ocr.parser import OCRParser

paddle_engine = PaddleOCREngine()
raw = paddle_engine.extract_text("data/raw/notes.png")

parser = OCRParser()

parsed = parser.parse(raw)

from pprint import pprint
pprint(parsed[:5])