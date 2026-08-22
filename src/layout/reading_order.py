
def sort_reading_order(ocr_results):
    return sorted(
        ocr_results,
        key=lambda item: (
            item["bbox"][1],
            item["bbox"][0]
        )
    )