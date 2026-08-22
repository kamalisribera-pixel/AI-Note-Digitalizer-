from .paragraph import Paragraph


class ParagraphGrouping:

    def __init__(self, line_gap_threshold=30):

        self.line_gap_threshold = line_gap_threshold


    def group(self, lines):

        if not lines:
            return []

        paragraphs = []

        current_paragraph = [lines[0]]

        for i in range(1, len(lines)):

            previous = lines[i - 1]
            current = lines[i]

            if self._same_paragraph(
                previous,
                current
            ):

                current_paragraph.append(current)

            else:

                paragraphs.append(
                    Paragraph(current_paragraph)
                )

                current_paragraph = [current]


        paragraphs.append(
            Paragraph(current_paragraph)
        )

        return paragraphs
    def _same_paragraph(
        self,
        previous,
        current
    ):

        previous_bottom = max(
            block.bounding_box[3]
            for block in previous.blocks
        )

        current_top = min(
            block.bounding_box[1]
            for block in current.blocks
        )

        gap = current_top - previous_bottom

        return gap <= self.line_gap_threshold