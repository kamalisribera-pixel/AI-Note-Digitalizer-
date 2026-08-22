from PIL import Image
from src.ocr.trocr_engine import TrOCREngine

engine = TrOCREngine()

image = Image.open(
    "data/raw/notes.png"
).convert("RGB")

result = engine.extract_text(image)

print(result)