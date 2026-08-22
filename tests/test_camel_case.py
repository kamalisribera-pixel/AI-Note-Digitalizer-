from src.document.paragraph.space_corrector.candidate_generation.generators.camel_case import CamelCaseGenerator
from  src.document.paragraph.merged_line import MergedLine


class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0, 0, 10, 10)


def test_camel_case():

    line = MergedLine(
        text="flightDataAnalysis",
        blocks=[
            MockBlock("flightDataAnalysis")
        ]
    )


    generator = CamelCaseGenerator()

    candidates = generator.generate(line)


    for candidate in candidates:
        print(candidate)


if __name__ == "__main__":
    test_camel_case()