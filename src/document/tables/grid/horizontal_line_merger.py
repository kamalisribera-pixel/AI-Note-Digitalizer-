class HorizontalLineMerger:

    def __init__(
        self,
        y_tolerance=3,
        gap_tolerance=5
    ):
        self.y_tolerance = y_tolerance
        self.gap_tolerance = gap_tolerance


    def merge(self, lines):

        if not lines:
            return []

        # Sort by y then x
        lines = sorted(
            lines,
            key=lambda l: (l.y, l.x1)
        )

        merged = []

        current = lines[0]

        for line in lines[1:]:

            same_y = (
                abs(current.y - line.y)
                <= self.y_tolerance
            )

            close_gap = (
                line.x1 - current.x2
                <= self.gap_tolerance
            )

            if same_y and close_gap:

                # extend current line
                current.x2 = max(
                    current.x2,
                    line.x2
                )

            else:

                merged.append(current)
                current = line

        merged.append(current)

        return merged