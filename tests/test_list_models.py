from src.document.lists.list_item import ListItem
from src.document.lists.list_block import ListBlock


def test_list_models():

    items = [
        ListItem(
            "Neural Networks",
            "•",
            0
        ),
        ListItem(
            "Transformers",
            "-",
            1
        )
    ]


    block = ListBlock(
        "bullet",
        items
    )


    print(block)


if __name__ == "__main__":
    test_list_models()