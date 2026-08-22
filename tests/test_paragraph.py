from src.layout.structure import DocumentBlock
from src.layout.paragraph import reconstruct_paragraphs


def test_paragraph_reconstruction():

    blocks = [

        DocumentBlock(
            "Artificial",
            "paragraph",
            [100,100,200,120]
        ),

        DocumentBlock(
            "Neural",
            "paragraph",
            [100,125,200,145]
        ),

        DocumentBlock(
            "Networks",
            "paragraph",
            [100,150,250,170]
        )

    ]


    result = reconstruct_paragraphs(blocks)




    assert len(result) == 1

    assert result[0].text == "Artificial Neural Networks"


if __name__ == "__main__":
    test_paragraph_reconstruction()
    print("paragraph reconstruction test passed")