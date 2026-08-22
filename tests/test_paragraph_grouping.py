from  src.document.paragraph.merged_line import MergedLine
from src.document.paragraph.paragraph_grouper import ParagraphGrouping


class MockBlock:

    def __init__(self, text, bbox):
        self.text = text
        self.bounding_box = bbox


def create_line(text, y):

    block = MockBlock(
        text,
        (10, y, 100, y + 20)
    )

    return MergedLine(
        text=text,
        blocks=[block]
    )


def test_paragraph_grouping():

    lines = [
        create_line("Artificial Neural Networks", 10),
        create_line("are computing systems", 40),
        create_line("inspired by the brain", 70),

        # big gap → new paragraph
        create_line("Chapter 2", 150)
    ]


    grouping = ParagraphGrouping(
        line_gap_threshold=30
    )

    paragraphs = grouping.group(lines)


    for i, paragraph in enumerate(paragraphs):

        print(f"Paragraph {i+1}:")
        print(paragraph.text)
        print("----------------")


if __name__ == "__main__":
    test_paragraph_grouping()