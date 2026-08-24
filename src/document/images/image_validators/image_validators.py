class ImageValidator:

    def __init__(
        self,
        vision,
        geometry,
        ocr,
        shape,
        layout,
        decision_engine
    ):

        self.vision = vision
        self.geometry = geometry
        self.ocr = ocr
        self.shape = shape
        self.layout = layout
        self.decision_engine = decision_engine


    def validate(self, image, image_block):

        evidences = []


        evidences.append(
            self.vision.evaluate(
                image,
                image_block
            )
        )


        evidences.append(
            self.geometry.evaluate(
                image,
                image_block
            )
        )


        evidences.append(
            self.ocr.evaluate(
                image,
                image_block
            )
        )


        evidences.append(
            self.shape.evaluate(
                image,
                image_block
            )
        )


        evidences.append(
            self.layout.evaluate(
                image,
                image_block
            )
        )


        decision = self.decision_engine.calculate(
            evidences
        )


        image_block.image_type = (
            decision["type"]
        )

        image_block.confidence = (
            decision["confidence"]
        )


        image_block.metadata = {
            "evidence": evidences,
            "decision": decision
        }


        return image_block