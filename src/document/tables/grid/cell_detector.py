class Cell:
    def __init__(self, row, column, bbox):
        self.row = row
        self.column = column
        self.bbox = bbox

    def __repr__(self):
        return (
            f"Cell("
            f"row={self.row}, "
            f"column={self.column}, "
            f"bbox={self.bbox})"
        )


def detect_cells(intersections):

    cells = []

    # Group intersections by y position
    rows = {}

    for point in intersections:
        rows.setdefault(point.y, []).append(point)

    # Sort rows top to bottom
    sorted_rows = sorted(rows.items())

    for row_index in range(len(sorted_rows) - 1):

        _, top_points = sorted_rows[row_index]
        _, bottom_points = sorted_rows[row_index + 1]

        # Sort points left to right
        top_points.sort(key=lambda p: p.x)
        bottom_points.sort(key=lambda p: p.x)

        for col_index in range(len(top_points) - 1):

            x1 = top_points[col_index].x
            x2 = top_points[col_index + 1].x

            y1 = sorted_rows[row_index][0]
            y2 = sorted_rows[row_index + 1][0]

            cell = Cell(
                row=row_index,
                column=col_index,
                bbox=(x1, y1, x2, y2)
            )

            cells.append(cell)

    return cells