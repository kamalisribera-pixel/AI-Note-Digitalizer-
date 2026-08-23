class CellExtractor:

    def extract(self, image, cells):

        extracted_cells = []

        for cell in cells:

            x1, y1, x2, y2 = cell.bbox

            crop = image[
                y1:y2,
                x1:x2
            ]

            extracted_cells.append(
                {
                    "cell": cell,
                    "image": crop
                }
            )

        return extracted_cells