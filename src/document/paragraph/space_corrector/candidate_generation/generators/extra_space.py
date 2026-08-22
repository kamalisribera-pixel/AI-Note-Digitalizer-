from ..spacing_candidate import SpacingCandidate


class ExtraSpaceGenerator:

    def generate(
        self,
        line,
        paragraph=None
    ):

        candidates = []

        words = line.text.split()

        if len(words) < 2:
            return candidates


        for i in range(len(words) - 1):

            left = words[i]
            right = words[i + 1]


            joined = (
                " ".join(words[:i])
                + " "
                + left + right
                + " "
                + " ".join(words[i+2:])
            ).strip()


            candidates.append(
                SpacingCandidate(
                    original_line=line,
                    candidate_text=joined,
                    source="extra_space",
                    split_positions=[],
                    paragraph=paragraph
                )
            )


        return candidates