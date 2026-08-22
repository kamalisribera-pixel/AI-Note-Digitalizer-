from pprint import pprint

from attr import dataclass

@dataclass
class OCRParser:
    def parse(self,result):
        parsed = []

        if not result:
            return parsed
        data = result[0]
        texts = data["rec_texts"]
        scores = data["rec_scores"]
        boxes = data["rec_boxes"]

        for text, score, box in zip(texts, scores, boxes):
            parsed.append({
                "text": text,
                "confidence": float(score),
                "bounding_box": box.tolist()
            })
        
        pprint(data.keys())
        return parsed


