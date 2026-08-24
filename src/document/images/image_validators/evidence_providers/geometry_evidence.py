from src.document.tables.grid.grid_extractor import GridExtractor


class GeometryEvidence:

    def __init__(self):

        self.grid_extractor = GridExtractor()


    def evaluate(self, image, image_block):

        x1, y1, x2, y2 = image_block.bbox

        crop = image[
            y1:y2,
            x1:x2
        ]

        grid = self.grid_extractor.extract(crop)

        score = 0.0

        if grid is not None:

            if len(grid.cells) > 0:
                score += 0.5

            if len(grid.intersections) > 0:
                score += 0.3

            if (
                len(grid.horizontal_lines) > 0 and
                len(grid.vertical_lines) > 0
            ):
                score += 0.2


        return {
            "source": "geometry",
            "type": "table",
            "score": min(score, 1.0)
        }