from src.document.paragraph.space_corrector.context.deberta_loader import DebertaLoader


def test_deberta_loader():

    loader = DebertaLoader()

    tokenizer, model = loader.load()

    print(type(tokenizer).__name__)
    print(type(model).__name__)


if __name__ == "__main__":
    test_deberta_loader()