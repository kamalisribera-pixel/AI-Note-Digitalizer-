import cv2

from src.document.tables.grid.grid_extractor import GridExtractor


def main():

    image = cv2.imread(
        "tests/images/grid/simple.png"
    )

    if image is None:
        print("Image not found")
        return

    extractor = GridExtractor()

    grid = extractor.extract(image)

    print("\nGRID RESULT")
    print(grid)

    print("\nHorizontal Lines:")
    for line in grid.horizontal_lines:
        print(line)

    print("\nVertical Lines:")
    for line in grid.vertical_lines:
        print(line)

    print("\nIntersections:")
    for point in grid.intersections:
        print(point)

    print("\nCells:")
    for cell in grid.cells:
        print(cell)

    print("\nMerged Cells:")
    for merged in grid.merged_cells:
        print(merged)


if __name__ == "__main__":
    main()