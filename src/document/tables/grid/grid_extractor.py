from .preprocess import preprocess_table
from .horizontal_detector import detect_horizontal_lines
from .vertical_detector import detect_vertical_lines
from .intersection_detection import detect_intersections
from .cell_detector import detect_cells
from .merged_cell_detector import detect_merged_cells
from .vertical_line_merger import VerticalLineMerger
from .horizontal_line_merger import HorizontalLineMerger


class Grid:
    def __init__(
        self,
        horizontal_lines,
        vertical_lines,
        intersections,
        cells,
        merged_cells
    ):
        self.horizontal_lines = horizontal_lines
        self.vertical_lines = vertical_lines
        self.intersections = intersections
        self.cells = cells
        self.merged_cells = merged_cells

    def __repr__(self):
        return (
            f"Grid("
            f"horizontal={len(self.horizontal_lines)}, "
            f"vertical={len(self.vertical_lines)}, "
            f"intersections={len(self.intersections)}, "
            f"cells={len(self.cells)}, "
            f"merged={len(self.merged_cells)})"
        )




class GridExtractor:

    def extract(self, image):

        binary = preprocess_table(image)

        horizontal_lines = detect_horizontal_lines(binary)

        horizontal_merger = HorizontalLineMerger()

        horizontal_lines = horizontal_merger.merge(
            horizontal_lines
        )

        vertical_lines = detect_vertical_lines(binary)

        vertical_merger = VerticalLineMerger()

        vertical_lines = vertical_merger.merge(
            vertical_lines
        )

        intersections = detect_intersections(
            horizontal_lines,
            vertical_lines
        )

        cells = detect_cells(
            intersections
        )

        merged_cells = detect_merged_cells(
            cells,
            horizontal_lines,
            vertical_lines
        )

        return Grid(
            horizontal_lines,
            vertical_lines,
            intersections,
            cells,
            merged_cells
        )