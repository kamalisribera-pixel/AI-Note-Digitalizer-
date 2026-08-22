from .spacing_candidate import SpacingCandidate


class CandidateGenerator:

    def __init__(self, generators):

        self.generators = generators


    def generate(
        self,
        line,
        paragraph=None
    ):

        candidates = [

            SpacingCandidate(
                original_line=line,
                candidate_text=line.text,
                source="original",
                split_positions=[]
            )

        ]


        for generator in self.generators:

            generated = generator.generate(
                line,
                paragraph
            )

            candidates.extend(
                generated
            )


        return candidates