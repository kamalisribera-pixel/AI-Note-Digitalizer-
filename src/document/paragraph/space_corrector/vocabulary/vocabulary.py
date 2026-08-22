class Vocabulary:

    def __init__(
        self,
        words=None
    ):

        self.words = set()

        if words:

            self.words.update(
                word.lower()
                for word in words
            )


    def contains(
        self,
        word
    ):

        return (
            word.lower()
            in self.words
        )


    def add(
        self,
        word
    ):

        self.words.add(
            word.lower()
        )


    def size(self):

        return len(self.words)