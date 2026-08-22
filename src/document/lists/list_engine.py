from .list_detector import ListDetector


class ListEngine:


    def __init__(
        self,
        detector=None
    ):

        self.detector = detector or ListDetector()



    def process(
        self,
        lines
    ):

        return self.detector.detect(
            lines
        )