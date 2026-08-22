class DecisionEngine:

    def __init__(
        self,
        geometry_weight=0.3,
        lexical_weight=0.4,
        context_weight=0.3
    ):

        self.geometry_weight = geometry_weight
        self.lexical_weight = lexical_weight
        self.context_weight = context_weight


    def evaluate(self, candidate):

        score = (
            candidate.geometry_score *
            self.geometry_weight
            +
            candidate.lexical_score *
            self.lexical_weight
            +
            candidate.context_score *
            self.context_weight
        )

        candidate.final_score = score

        return score