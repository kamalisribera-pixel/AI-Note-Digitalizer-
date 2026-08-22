from src.engine.layout_engine import LayoutEngine


def test_layout_engine():

    ocr_results = [
        {
            "text": "Neural Networks",
            "bbox": [100, 0, 500, 60],
            "confidence": 0.95
        },
        {
            "text": "A neuron receives signals",
            "bbox": [100, 80, 500, 110],
            "confidence": 0.92
        }
    ]


    engine = LayoutEngine()

    result = engine.analyze(
        ocr_results
    )


    assert len(result) == 2

    assert result[0].text == "Neural Networks"

    assert result[1].text == "A neuron receives signals"


if __name__ == "__main__":
    test_layout_engine()
    print("layout engine test passed")