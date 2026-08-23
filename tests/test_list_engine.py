from src.document.lists.list_engine import ListEngine
from src.document.paragraph.merged_line import MergedLine
from layout.text_block import TextBlock
def test_list_engine():

    lines = [

        MergedLine(
            "• Neural Networks",
            []
        ),

        MergedLine(
            "• Transformers",
            []
        ),

        MergedLine(
            "• RAG",
            []
        )

    ]


    engine = ListEngine()


    result = engine.process(
        lines
    )


    print(result)



if __name__ == "__main__":
    test_list_engine()