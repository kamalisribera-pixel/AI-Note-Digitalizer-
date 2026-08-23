import cv2

from src.document.tables.grid.grid_extractor import GridExtractor
from src.document.tables.table_detector import TableDetector


image = cv2.imread(
    "tests/images/grid/simple.png"
)

grid_extractor = GridExtractor()

grid = grid_extractor.extract(image)


detector = TableDetector()

table = detector.detect(grid)


print("TABLE RESULT")
print(table)