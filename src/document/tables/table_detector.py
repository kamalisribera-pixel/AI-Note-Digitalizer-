from .table_block import TableRegion


class TableDetector:

    def detect(self, grid):

        if grid is None:
            return None

        if not grid.cells:
            return None

        x_values = []
        y_values = []

        for cell in grid.cells:

            x1, y1, x2, y2 = cell.bbox

            x_values.extend([
                x1,
                x2
            ])

            y_values.extend([
                y1,
                y2
            ])

        bbox = (
            min(x_values),
            min(y_values),
            max(x_values),
            max(y_values)
        )

        return TableRegion(
            bbox=bbox,
            confidence=1.0
        )