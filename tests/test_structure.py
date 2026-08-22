from src.layout.structure import DocumentBlock


def test_document_block():

    block = DocumentBlock(
        text="Artificial Neural Networks",
        block_type="heading",
        bbox=[227, 0, 598, 34],
        confidence=0.95
    )

    result = block.to_dict()

    assert result["text"] == "Artificial Neural Networks"
    assert result["type"] == "heading"
    assert result["bbox"] == [227, 0, 598, 34]
    assert result["confidence"] == 0.95


if __name__ == "__main__":
    test_document_block()
    print("structure test passed")