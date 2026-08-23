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

    # Group intersections by y coordinate
    rows = {}

    for point in intersections:
        rows.setdefault(point.y, []).append(point)

    # Sort rows top to bottom
    sorted_rows = sorted(rows.items(), key=lambda item: item[0])

    for row_index in range(len(sorted_rows) - 1):

        top_y, top_points = sorted_rows[row_index]
        bottom_y, bottom_points = sorted_rows[row_index + 1]

        # Sort intersections left to right
        top_points.sort(key=lambda p: p.x)
        bottom_points.sort(key=lambda p: p.x)

        for col_index in range(len(top_points) - 1):

            left = top_points[col_index]
            right = top_points[col_index + 1]

            cell = Cell(
                row=row_index,
                column=col_index,
                bbox=(
                    left.x,
                    top_y,
                    right.x,
                    bottom_y
                )
            )

            cells.append(cell)

    return cells