class EnglishVocabulary:

    def __init__(self, words):

        self.words = {
            word.lower()
            for word in words
        }


    def contains(self, word):

        word = word.lower().strip()

        return word in self.words