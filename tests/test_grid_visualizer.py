import cv2

from src.document.tables.grid.grid_extractor import GridExtractor
from src.document.tables.grid.grid_visualizer import draw_grid


image = cv2.imread(
    "tests/images/grid/simple.png"
)


extractor = GridExtractor()

grid = extractor.extract(image)


result = draw_grid(
    image,
    grid
)


cv2.imshow(
    "Grid Visualization",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()