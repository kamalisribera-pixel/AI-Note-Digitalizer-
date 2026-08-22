from src.document.paragraph.space_corrector.candidate_generation.generators.extra_space import ExtraSpaceGenerator
from  src.document.paragraph.merged_line import MergedLine


class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0, 0, 10, 10)


def test_extra_space():

    line = MergedLine(
        text="Artificial Ne ural Networks",
        blocks=[
            MockBlock("Artificial"),
            MockBlock("Ne"),
            MockBlock("ural"),
            MockBlock("Networks")
        ]
    )


    generator = ExtraSpaceGenerator()

    candidates = generator.generate(line)


    for candidate in candidates:
        print(candidate)


if __name__ == "__main__":
    test_extra_space()