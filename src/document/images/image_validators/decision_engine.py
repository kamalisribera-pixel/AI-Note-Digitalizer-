class DecisionEngine:

    def __init__(self):

        self.weights = {
            "vision": 0.20,
            "geometry": 0.25,
            "ocr": 0.20,
            "shape": 0.15,
            "layout": 0.20
        }


    def calculate(self, evidences):

        scores = {}

        for evidence in evidences:

            image_type = evidence["type"]
            source = evidence["source"]
            score = evidence["score"]


            if image_type not in scores:
                scores[image_type] = 0.0


            weight = self.weights.get(
                source,
                0
            )


            scores[image_type] += (
                score * weight
            )


        best_type = max(
            scores,
            key=scores.get
        )


        return {
            "type": best_type,
            "confidence": scores[best_type],
            "all_scores": scores
        }