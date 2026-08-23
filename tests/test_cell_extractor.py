import cv2

from src.document.tables.grid.grid_extractor import GridExtractor
from src.document.tables.cell_extractor import CellExtractor


image = cv2.imread(
    "tests/images/grid/simple.png"
)


grid_extractor = GridExtractor()

grid = grid_extractor.extract(image)


extractor = CellExtractor()

cells = extractor.extract(
    image,
    grid.cells
)


print("CELL RESULT")
print("Total cells:", len(cells))


for i, item in enumerate(cells[:3]):

    cell = item["cell"]
    crop = item["image"]

    print(
        f"Cell {i}:",
        f"bbox={cell.bbox}",
        f"shape={crop.shape}"
    )