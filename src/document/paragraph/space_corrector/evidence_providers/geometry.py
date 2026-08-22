class GeometryProvider:

    name = "geometry"


    def score(self, candidate):

        line = candidate.original_line

        blocks = line.blocks


        if not blocks:
            return 0.0


        # OCR already detected separate regions
        visual_words = len(blocks)

        candidate_words = len(
            candidate.candidate_text.split()
        )


        # closer word count means better geometry
        difference = abs(
            visual_words - candidate_words
        )


        score = 1 / (1 + difference)


        return score