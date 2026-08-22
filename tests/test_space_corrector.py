from src.document.paragraph.paragraph import Paragraph

from src.document.paragraph.space_corrector.candidate_generation.generators.missing_space import MissingSpaceGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.extra_space import ExtraSpaceGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.camel_case import CamelCaseGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.long_word import LongWordGenerator
from src.document.paragraph.space_corrector.candidate_generation.candidate_generator import CandidateGenerator
from src.document.paragraph.merged_line import MergedLine

from src.document.paragraph.space_corrector.space_corrector import SpaceCorrector

from src.document.paragraph.space_corrector.decision_engine import DecisionEngine





class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0,0,10,10)

class MockGeometry:

    name = "geometry"

    def score(self, candidate):
        return 0.5


class MockLexical:

    name = "lexical"

    def score(self, candidate):
        if "flight Data Analysis" in candidate.candidate_text:
            return 1.0

        return 0.1



class MockContext:

    name = "context"

    def score(self, candidate):
        if "flight Data Analysis" in candidate.candidate_text:
            return 1.0

        return 0.2



def test_space_corrector():

    line = MergedLine(
        text="flightDataAnalysis",
        blocks=[
            MockBlock(
                "flightDataAnalysis"
            )
        ]
    )


    paragraph = Paragraph(
        [
            line
        ]
    )


    candidate_generator = CandidateGenerator(
        [
            MissingSpaceGenerator(),
            ExtraSpaceGenerator(),
            CamelCaseGenerator(),
            LongWordGenerator()
        ]
    )


    corrector = SpaceCorrector(
        candidate_generator,
        [
            MockGeometry(),
            MockLexical(),
            MockContext()
        ],
        DecisionEngine()
    )


    result = corrector.correct(
        paragraph
    )


    print(result)



if __name__ == "__main__":
    test_space_corrector()