from src.document.tables.grid.grid_extractor import GridExtractor


class LayoutEvidence:

    def __init__(self):

        self.grid_extractor = GridExtractor()


    def evaluate(self, image, image_block):

        x1, y1, x2, y2 = image_block.bbox

        crop = image[
            y1:y2,
            x1:x2
        ]


        grid = self.grid_extractor.extract(
            crop
        )


        score = 0.0

        details = {
            "cells": 0,
            "rows": 0,
            "columns": 0
        }


        if grid:

            cells = grid.cells

            details["cells"] = len(cells)


            if len(cells) >= 2:
                score += 0.4


            rows = set()
            columns = set()


            for cell in cells:

                x1, y1, x2, y2 = cell.bbox

                rows.add(
                    y1
                )

                columns.add(
                    x1
                )
                


            details["rows"] = len(rows)
            details["columns"] = len(columns)


            if len(rows) >= 2:
                score += 0.25


            if len(columns) >= 1:
                score += 0.2


        if len(rows) > 1 and len(cells) == len(rows):
            score += 0.15

        return {
            "source": "layout",
            "type": "table",
            "score": min(score, 1.0),
            "details": details
        }