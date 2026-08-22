

from src.ocr.paddle_engine import PaddleOCREngine


result = PaddleOCREngine().extract_text("data/raw/notes.png")

print(result)