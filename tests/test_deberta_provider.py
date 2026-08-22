from src.document.paragraph.space_corrector.context.deberta_provider import DebertaProvider
from src.document.paragraph.space_corrector.candidate_generation.spacing_candidate import SpacingCandidate


class MockLine:

    def __init__(self, text):
        self.text = text


def test_deberta_provider():

    provider = DebertaProvider()

    line = MockLine(
        "flightDataAnalysis is important."
    )

    candidate = SpacingCandidate(
        original_line=line,
        candidate_text="flight Data Analysis is important.",
        source="test",
        split_positions=[]
    )

    score = provider.score(candidate)

    print("Context score:", score)


if __name__ == "__main__":
    test_deberta_provider()