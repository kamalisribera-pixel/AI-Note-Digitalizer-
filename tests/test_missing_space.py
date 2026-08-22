from src.document.paragraph.space_corrector.candidate_generation.generators.missing_space import MissingSpaceGenerator
from  src.document.paragraph.merged_line import MergedLine


class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0, 0, 10, 10)


def test_missing_space():

    line = MergedLine(
        text="ArtificialNeuralNetworks",
        blocks=[
            MockBlock("ArtificialNeuralNetworks")
        ]
    )


    generator = MissingSpaceGenerator()

    candidates = generator.generate(line)


    for candidate in candidates:
        print(candidate)


if __name__ == "__main__":
    test_missing_space()