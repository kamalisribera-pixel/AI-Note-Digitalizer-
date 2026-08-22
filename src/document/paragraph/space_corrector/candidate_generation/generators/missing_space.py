from ..spacing_candidate import SpacingCandidate


class MissingSpaceGenerator:

    def generate(
        self,
        line,
        paragraph=None
    ):

        candidates = []

        text = line.text

        splits = self._find_splits(text)


        for split_text, positions in splits:

            candidates.append(
                SpacingCandidate(
                    original_line=line,
                    candidate_text=split_text,
                    source="missing_space",
                    split_positions=positions,
                    paragraph=paragraph
                )
            )


        return candidates
    def _find_splits(self, text):

        candidates = []

        for i in range(2, len(text) - 2):

            left = text[:i]
            right = text[i:]

            candidates.append(
                (
                    left + " " + right,
                    [i]
                )
            )

        return candidates