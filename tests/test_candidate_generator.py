from src.document.paragraph.space_corrector.candidate_generation.generators.missing_space import MissingSpaceGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.extra_space import ExtraSpaceGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.camel_case import CamelCaseGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.long_word import LongWordGenerator
from src.document.paragraph.space_corrector.candidate_generation.candidate_generator import CandidateGenerator
from src.document.paragraph.merged_line import MergedLine


class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0, 0, 10, 10)



def test_candidate_generator():

    line = MergedLine(
        text="flightDataAnalysis",
        blocks=[
            MockBlock("flightDataAnalysis")
        ]
    )


    generator = CandidateGenerator(
        [
            MissingSpaceGenerator(),
            ExtraSpaceGenerator(),
            CamelCaseGenerator(),
            LongWordGenerator()
        ]
    )


    candidates = generator.generate(line)


    for candidate in candidates:
        print(candidate)



if __name__ == "__main__":
    test_candidate_generator()