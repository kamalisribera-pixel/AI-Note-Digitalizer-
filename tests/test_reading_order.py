from src.layout.reading_order import sort_reading_order


def test_reading_order():

    ocr_results = [
        {
            "text": "Bottom Text",
            "bbox": [50, 300, 200, 330]
        },
        {
            "text": "Title",
            "bbox": [50, 10, 300, 40]
        },
        {
            "text": "Middle Text",
            "bbox": [50, 150, 250, 180]
        }
    ]


    result = sort_reading_order(ocr_results)


    assert result[0]["text"] == "Title"
    assert result[1]["text"] == "Middle Text"
    assert result[2]["text"] == "Bottom Text"


if __name__ == "__main__":
    test_reading_order()
    print("reading order test passed")