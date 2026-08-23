class VerticalLineMerger:

    def __init__(
        self,
        x_tolerance=3,
        gap_tolerance=5
    ):
        self.x_tolerance = x_tolerance
        self.gap_tolerance = gap_tolerance


    def merge(self, lines):

        if not lines:
            return []

        # Sort by x then y
        lines = sorted(
            lines,
            key=lambda l: (l.x, l.y1)
        )

        merged = []

        current = lines[0]

        for line in lines[1:]:

            same_x = (
                abs(current.x - line.x)
                <= self.x_tolerance
            )

            close_gap = (
                line.y1 - current.y2
                <= self.gap_tolerance
            )

            if same_x and close_gap:

                # extend current line
                current.y2 = max(
                    current.y2,
                    line.y2
                )

            else:

                merged.append(current)
                current = line

        merged.append(current)

        return merged