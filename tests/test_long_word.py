

from src.document.paragraph.space_corrector.candidate_generation.generators.long_word import LongWordGenerator
from src.document.paragraph.space_corrector.vocabulary.vocabulary import Vocabulary

from src.document.paragraph.merged_line import MergedLine



class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0, 0, 10, 10)



def test_long_word():

    vocab = Vocabulary(
        [
            "artificial",
            "neural",
            "network"
        ]
    )


    line = MergedLine(
        text="artificialneuralnetwork",
        blocks=[
            MockBlock(
                "artificialneuralnetwork"
            )
        ]
    )


    generator = LongWordGenerator(
        vocab
    )


    candidates = generator.generate(
        line
    )


    for candidate in candidates:
        print(candidate)



if __name__ == "__main__":
    test_long_word()