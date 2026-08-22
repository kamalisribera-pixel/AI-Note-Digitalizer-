from .merged_line import MergedLine
class LineMerger:

    LINE_THRESHOLD = 15

    def merge(self, blocks):

        if not blocks:
            return []

        blocks = sorted(
            blocks,
            key=lambda b: (b.bounding_box[1] + b.bounding_box[3]) / 2
        )

        rows = []
        current_row = []

        current_y = None

        for block in blocks:

            center_y = (block.bounding_box[1] + block.bounding_box[3]) / 2

            if current_y is None:
                current_row.append(block)
                current_y = center_y

            elif abs(center_y - current_y) <= self.LINE_THRESHOLD:
                current_row.append(block)

            else:
                rows.append(current_row)
                current_row = [block]
                current_y = center_y

        rows.append(current_row)

        merged_lines = []

        for row in rows:

            row.sort(key=lambda b: b.bounding_box[0])

            merged_lines.append(
                MergedLine(
                    text=" ".join(block.text for block in row),
                    blocks=row
                )
            )

        return merged_lines