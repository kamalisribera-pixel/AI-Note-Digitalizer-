from src.document.paragraph.sentence_reconstructor import SentenceReconstruction
from src.document.paragraph.merged_line import MergedLine



class MockBlock:

    def __init__(self, text):
        self.text = text
        self.bounding_box = (0,0,10,10)



def test_sentence_reconstruction():

    lines = [

        MergedLine(
            "Artificial Neural Networks are",
            [MockBlock("Artificial Neural Networks are")]
        ),

        MergedLine(
            "computing systems inspired by the",
            [MockBlock("computing systems inspired by the")]
        ),

        MergedLine(
            "human brain.",
            [MockBlock("human brain.")]
        )
    ]


    reconstructor = SentenceReconstruction()

    result = reconstructor.reconstruct(
        lines
    )


    print(result)



if __name__ == "__main__":
    test_sentence_reconstruction()