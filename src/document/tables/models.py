class TableRegion:

    def __init__(self, bbox, confidence=1.0):
        self.bbox = bbox
        self.confidence = confidence

    def __repr__(self):
        return (
            f"TableRegion("
            f"bbox={self.bbox}, "
            f"confidence={self.confidence}"
            f")"
        )