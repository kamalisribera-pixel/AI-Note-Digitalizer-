import cv2

from src.document.tables.grid.grid_extractor import GridExtractor
from src.document.tables.cell_extractor import CellExtractor
from src.document.tables.cell_ocr import CellOCR


image = cv2.imread(
    "tests/images/grid/simple.png"
)


grid = GridExtractor().extract(image)

cells = CellExtractor().extract(
    image,
    grid.cells
)


ocr = CellOCR()

results = ocr.extract_text(cells)


print("OCR RESULT")

for item in results[:3]:
    print(
        item["text"]
    )