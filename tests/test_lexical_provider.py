from src.document.paragraph.space_corrector.evidence_providers.lexical import LexicalProvider
from src.document.paragraph.space_corrector.vocabulary.vocabulary import Vocabulary

from src.document.paragraph.space_corrector.candidate_generation.spacing_candidate import SpacingCandidate



class MockLine:

    def __init__(self, text):
        self.text = text



def test_lexical_provider():

    vocab = Vocabulary(
        [
            "flight",
            "data",
            "analysis",
            "important"
        ]
    )


    provider = LexicalProvider(
        vocab
    )


    candidate = SpacingCandidate(
        original_line=MockLine(
            "flightDataAnalysis"
        ),
        candidate_text="flight Data Analysis",
        source="camel_case",
        split_positions=[6,10]
    )


    score = provider.score(
        candidate
    )


    print(score)



if __name__ == "__main__":
    test_lexical_provider()