from src.document.paragraph.line_merger import LineMerger
from src.layout.structure import TextBlock


def test_line_merger():

    merger = LineMerger()

    blocks = [

        TextBlock(
            text="Artificial Neural Networks",
            bounding_box=[227, 0, 598, 34],
            confidence=0.84
        ),

        TextBlock(
            text="Biological Mesron: sends + receive + itransrit",
            bounding_box=[4, 30, 386, 68],
            confidence=0.91
        ),

        TextBlock(
            text="anon",
            bounding_box=[549, 26, 599, 53],
            confidence=0.98
        ),

        TextBlock(
            text="synapses",
            bounding_box=[631, 22, 705, 56],
            confidence=0.90
        ),

        TextBlock(
            text="passes relectrical",
            bounding_box=[9, 58, 170, 87],
            confidence=0.91
        )

    ]

    merged = merger.merge(blocks)

    print("\nMerged Lines:")
    for line in merged:
        print(line)

    assert len(merged) == 3

    print("\n✓ Line Merger Test Passed")


if __name__ == "__main__":
    test_line_merger()