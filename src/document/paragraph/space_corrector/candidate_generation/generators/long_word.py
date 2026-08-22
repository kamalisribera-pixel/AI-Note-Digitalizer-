from ..spacing_candidate import SpacingCandidate


class LongWordGenerator:

    def __init__(
        self,
        vocabulary,
        min_length=15
    ):

        self.vocabulary = vocabulary
        self.min_length = min_length



    def generate(
        self,
        line,
        paragraph=None
    ):

        candidates = []

        words = line.text.split()


        for word in words:

            if len(word) >= self.min_length:

                splits = self._segment(
                    word
                )


                if splits:

                    candidates.append(
                        SpacingCandidate(
                            original_line=line,
                            candidate_text=" ".join(splits),
                            source="long_word",
                            split_positions=[]
                        )
                    )


        return candidates



    def _segment(
        self,
        word
    ):

        result = []


        def search(
            remaining,
            current
        ):

            if not remaining:

                result.extend(
                    current
                )

                return True


            for i in range(
                len(remaining),
                1,
                -1
            ):

                part = remaining[:i]


                if self.vocabulary.contains(part):

                    if search(
                        remaining[i:],
                        current + [part]
                    ):

                        return True


            return False


        search(
            word.lower(),
            []
        )


        return result