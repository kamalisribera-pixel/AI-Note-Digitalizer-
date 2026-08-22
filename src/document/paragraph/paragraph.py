class Paragraph:

    def __init__(self, lines):

        self.lines = lines

        self.text = self._build_text()


    def _build_text(self):

        return "\n".join(
            line.text
            for line in self.lines
        )


    def __repr__(self):

        return (
            f"Paragraph("
            f"lines={len(self.lines)}, "
            f"text='{self.text[:50]}...'"
            f")"
        )