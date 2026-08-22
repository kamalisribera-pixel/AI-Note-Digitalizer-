class FrequencyVocabulary:

    def __init__(self, frequencies):

        self.frequencies = frequencies


    def score(self, word):

        word = word.lower().strip()

        frequency = self.frequencies.get(
            word,
            0
        )

        return self._normalize(frequency)


    def _normalize(self, frequency):

        if frequency == 0:
            return 0.0

        if frequency >= 100000:
            return 1.0

        return frequency / 100000

