from src.engine.ocr_pipeline import OCRPipeline


def test_pipeline():

    engine = OCRPipeline()

    result = engine.extract_text(
        "data/raw/notes.png"
    )

    print("\nRESULT COUNT:", len(result))

    for i, text in enumerate(result):
        print(i, ":", text)

    assert len(result) > 0