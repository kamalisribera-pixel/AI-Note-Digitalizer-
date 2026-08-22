from src.document.paragraph.space_corrector.vocabulary.vocabulary_loader import VocabularyLoader



def test_vocabulary_loader():

    loader = VocabularyLoader()

    vocab = loader.load_english(
        50000
    )


    print(
        "Vocabulary size:",
        vocab.size()
    )


    print(
        "neural:",
        vocab.contains("neural")
    )


    print(
        "computer:",
        vocab.contains("computer")
    )


    print(
        "xyzabc:",
        vocab.contains("xyzabc")
    )



if __name__ == "__main__":
    test_vocabulary_loader()