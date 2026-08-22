class SentenceReconstruction:

    def reconstruct(self, lines):

        if not lines:
            return ""

        sentence_parts = []

        for line in lines:

            text = " ".join(line.split())

            if text:
                sentence_parts.append(text)

        return " ".join(sentence_parts)