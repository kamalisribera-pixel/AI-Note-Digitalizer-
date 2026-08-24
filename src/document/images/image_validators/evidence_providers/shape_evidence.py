import cv2


class ShapeEvidence:

    def evaluate(self, image, image_block):

        x1, y1, x2, y2 = image_block.bbox

        crop = image[
            y1:y2,
            x1:x2
        ]

        gray = cv2.cvtColor(
            crop,
            cv2.COLOR_BGR2GRAY
        )

        edges = cv2.Canny(
            gray,
            50,
            150
        )

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )


        rectangles = 0

        for contour in contours:

            approx = cv2.approxPolyDP(
                contour,
                0.02 * cv2.arcLength(
                    contour,
                    True
                ),
                True
            )

            if len(approx) == 4:
                rectangles += 1


        score = 0.0


        # Tables, diagrams, flowcharts often have rectangles
        if rectangles > 0:
            score += 0.5


        # More shapes = stronger evidence
        if rectangles >= 3:
            score += 0.3


        if len(contours) > 5:
            score += 0.2


        return {
            "source": "shape",
            "type": "table",
            "score": min(score, 1.0),
            "details": {
                "rectangles": rectangles,
                "contours": len(contours)
            }
        }