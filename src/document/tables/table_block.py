from dataclasses import dataclass


@dataclass
class TableBlock:

    rows: list
    bbox: tuple
    confidence: float = 1.0

    def __repr__(self):
        return (
            f"TableBlock("
            f"rows={len(self.rows)}, "
            f"bbox={self.bbox}, "
            f"confidence={self.confidence}"
            f")"
        )