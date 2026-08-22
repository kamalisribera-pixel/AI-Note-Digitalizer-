from src.document.paragraph.paragraph import Paragraph
from src.document.paragraph.paragraph_engine import ParagraphEngine
from src.document.paragraph.line_merger import MergedLine 

from src.document.paragraph.space_corrector.space_corrector import SpaceCorrector
from src.document.paragraph.space_corrector.decision_engine import DecisionEngine

from src.document.paragraph.space_corrector.candidate_generation.candidate_generator import CandidateGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.missing_space import MissingSpaceGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.extra_space import ExtraSpaceGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.camel_case import CamelCaseGenerator
from src.document.paragraph.space_corrector.candidate_generation.generators.long_word import LongWordGenerator
from src.document.paragraph.space_corrector.evidence_providers.geometry import GeometryProvider

from src.document.paragraph.space_corrector.vocabulary.vocabulary_loader import VocabularyLoader
from src.document.paragraph.space_corrector.evidence_providers.lexical import LexicalProvider

from src.document.paragraph.space_corrector.context.deberta_provider import DebertaProvider

class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0, 0, 10, 10)


class MockGeometry:

    name = "geometry"

    def score(self, candidate):
        return 0.5


class MockContext:

    name = "context"

    def score(self, candidate):

        if "flight Data Analysis" in candidate.candidate_text:
            return 1.0

        return 0.2


def test_paragraph_engine():

    # Load the real English vocabulary
    loader = VocabularyLoader()

    vocab = loader.load_english(50000)

    lexical_provider = LexicalProvider(vocab)

    # Build OCR lines
    lines = [

        MergedLine(
            text="flightDataAnalysis",
            blocks=[
                MockBlock("flightDataAnalysis")
            ]
        ),

        MergedLine(
            text="is important.",
            blocks=[
                MockBlock("is important.")
            ]
        )

    ]

    paragraph = Paragraph(lines)

    # Candidate generator
    candidate_generator = CandidateGenerator(
        [
            MissingSpaceGenerator(),
            ExtraSpaceGenerator(),
            CamelCaseGenerator(),
            LongWordGenerator(vocab)
        ]
    )

    # Space corrector
    space_corrector = SpaceCorrector(
        candidate_generator,
        [
            GeometryProvider(),
            lexical_provider,
            DebertaProvider()
        ],
        DecisionEngine() 
    )

    # Paragraph engine
    engine = ParagraphEngine(
        space_corrector
    )

    result = engine.process(
        paragraph
    )

    print(result)


if __name__ == "__main__":
    test_paragraph_engine()