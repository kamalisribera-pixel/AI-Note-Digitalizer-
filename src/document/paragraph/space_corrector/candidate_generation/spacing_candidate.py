class SpacingCandidate:

    def __init__(
        self,
        original_line,
        candidate_text,
        source,
        split_positions=None,
        paragraph=None
    ):

        self.original_line = original_line
        self.candidate_text = candidate_text
        self.source = source

        # Where spaces were inserted/removed
        self.split_positions = split_positions or []

        # Paragraph context
        self.paragraph = paragraph

        # Evidence scores
        self.geometry_score = None
        self.lexical_score = None
        self.context_score = None

        # Final decision score
        self.final_score = None


    def __repr__(self):

        return (
            f"SpacingCandidate("
            f"candidate='{self.candidate_text}', "
            f"source='{self.source}', "
            f"splits={self.split_positions}"
            f")"
        )