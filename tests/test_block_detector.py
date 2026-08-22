from layout.block_detector import detect_blocks


def test_block_detection():

    ocr_results = [
        {
            "text":"Title",
            "bbox":[0,0,300,60],
            "confidence":0.9
        },
        {
            "text":"Normal text",
            "bbox":[0,80,300,100],
            "confidence":0.95
        }
    ]


    blocks = detect_blocks(ocr_results)


    assert blocks[0].block_type == "heading"
    assert blocks[1].block_type == "paragraph"


if __name__ == "__main__":
    test_block_detection()
    print("block detector test passed")