import string


class LexicalProvider:

    name = "lexical"

    def __init__(
        self,
        vocabulary
    ):

        self.vocabulary = vocabulary


    def score(
        self,
        candidate
    ):

        words = candidate.candidate_text.split()

        if not words:
            return 0.0

        valid = 0

        for word in words:

            # Remove punctuation from both ends
            cleaned = word.strip(
                string.punctuation
            )

            if not cleaned:
                continue

            if self.vocabulary.contains(cleaned):
                valid += 1

        return valid / len(words)