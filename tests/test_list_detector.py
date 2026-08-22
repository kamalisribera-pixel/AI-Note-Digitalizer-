from src.document.lists.list_detector import ListDetector
from src.document.paragraph.merged_line import MergedLine
from src.layout.structure import TextBlock


def test_list_detector():

    lines = [

        MergedLine(
            "• AI",
            [
                TextBlock(
                    "• AI",
                    [50,0,100,20]
                )
            ]
        ),

        MergedLine(
            "• Machine Learning",
            [
                TextBlock(
                    "• Machine Learning",
                    [70,25,200,45]
                )
            ]
        )
    ]

    detector = ListDetector()

    result = detector.detect(
        lines
    )


    print(result)


def test_numbered_list():

    lines = [

        MergedLine(
            "1. Install Python",
            []
        ),

        MergedLine(
            "2. Install PyTorch",
            []
        ),

        MergedLine(
            "3. Train Model",
            []
        )

    ]


    detector = ListDetector()

    result = detector.detect(
        lines
    )


    print(result)

def test_nested_list():

    lines = [

        MergedLine(
            "• AI",
            [
                TextBlock(
                    "• AI",
                    [50,0,100,20]
                )
            ]
        ),

        MergedLine(
            "• Deep Learning",
            [
                TextBlock(
                    "• Deep Learning",
                    [70,25,200,45]
                )
            ]
        ),

        MergedLine(
            "• Transformers",
            [
                TextBlock(
                    "• Transformers",
                    [90,50,220,70]
                )
            ]
        )

    ]


    detector = ListDetector()

    result = detector.detect(
        lines
    )


    print(result)

if __name__ == "__main__":
    test_list_detector()