from src.document.images.image_classifier import ImageClassifier
class VisionEvidence:

    def __init__(self):
        self.classifier = ImageClassifier()


    def evaluate(self, image, image_block):

        result = self.classifier.classify(
            image_block,
            image
        )


        return {
            "source": "vision",
            "type": result.image_type,
            "score": result.confidence
        }