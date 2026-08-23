class MergedCell:
    def __init__(self, cells, bbox):
        self.cells = cells
        self.bbox = bbox

    def __repr__(self):
        return (
            f"MergedCell("
            f"cells={len(self.cells)}, "
            f"bbox={self.bbox})"
        )


def has_vertical_border(x, y1, y2, vertical_lines):

    for line in vertical_lines:

        if abs(line.x - x) <= 2:

            if (
                line.y1 <= y1
                and line.y2 >= y2
            ):
                return True

    return False


def has_horizontal_border(y, x1, x2, horizontal_lines):

    for line in horizontal_lines:

        if abs(line.y - y) <= 2:

            if (
                line.x1 <= x1
                and line.x2 >= x2
            ):
                return True

    return False


def detect_merged_cells(
        cells,
        horizontal_lines,
        vertical_lines
):

    merged_cells = []

    visited = set()


    for cell in cells:

        if id(cell) in visited:
            continue


        group = [cell]

        x1, y1, x2, y2 = cell.bbox


        for other in cells:

            if other is cell:
                continue

            if id(other) in visited:
                continue


            ox1, oy1, ox2, oy2 = other.bbox


            # horizontal neighbour
            if (
                y1 == oy1
                and y2 == oy2
            ):

                border = has_vertical_border(
                    min(x2, ox1),
                    y1,
                    y2,
                    vertical_lines
                )

                if not border:
                    group.append(other)
                    visited.add(id(other))


            # vertical neighbour
            elif (
                x1 == ox1
                and x2 == ox2
            ):

                border = has_horizontal_border(
                    min(y2, oy1),
                    x1,
                    x2,
                    horizontal_lines
                )

                if not border:
                    group.append(other)
                    visited.add(id(other))


        if len(group) > 1:

            xs = []
            ys = []

            for c in group:

                cx1, cy1, cx2, cy2 = c.bbox

                xs.extend([cx1, cx2])
                ys.extend([cy1, cy2])


            merged_cells.append(
                MergedCell(
                    group,
                    (
                        min(xs),
                        min(ys),
                        max(xs),
                        max(ys)
                    )
                )
            )


        visited.add(id(cell))


    return merged_cells