class VocabularyManager:

    def __init__(
        self,
        english_vocab,
        frequency_vocab,
        domain_vocab
    ):

        self.english_vocab = english_vocab
        self.frequency_vocab = frequency_vocab
        self.domain_vocab = domain_vocab


    def score_word(self, word):

        score = 0.0

        if self.english_vocab.contains(word):
            score += 0.4

        score += self.frequency_vocab.score(word) * 0.3

        if self.domain_vocab.contains(word):
            score += 0.3

        return score