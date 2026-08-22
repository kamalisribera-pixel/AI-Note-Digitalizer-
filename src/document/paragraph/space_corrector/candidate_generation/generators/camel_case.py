from ..spacing_candidate import SpacingCandidate


class CamelCaseGenerator:

    def generate(
        self,
        line,
        paragraph=None
    ):

        candidates = []

        text = line.text

        split_positions = self._find_capital_positions(text)


        if not split_positions:
            return candidates


        candidate_text = self._insert_spaces(
            text,
            split_positions
        )


        candidates.append(
            SpacingCandidate(
                original_line=line,
                candidate_text=candidate_text,
                source="camel_case",
                split_positions=split_positions,
                paragraph=paragraph
            )
        )


        return candidates


    def _find_capital_positions(self, text):

        positions = []

        for i in range(1, len(text)):

            if text[i].isupper():

                positions.append(i)


        return positions


    def _insert_spaces(self, text, positions):

        result = text

        offset = 0

        for position in positions:

            result = (
                result[:position + offset]
                +
                " "
                +
                result[position + offset:]
            )

            offset += 1


        return result