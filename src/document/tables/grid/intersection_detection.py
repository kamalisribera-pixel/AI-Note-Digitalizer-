class Intersection:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Intersection(x={self.x}, y={self.y})"


def detect_intersections(horizontal_lines, vertical_lines):

    intersections = []

    for h_line in horizontal_lines:
        for v_line in vertical_lines:

            if (
                h_line.x1 <= v_line.x <= h_line.x2
                and v_line.y1 <= h_line.y <= v_line.y2
            ):
                intersections.append(
                    Intersection(
                        v_line.x,
                        h_line.y
                    )
                )

    return intersections