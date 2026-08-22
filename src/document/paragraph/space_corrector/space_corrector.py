class SpaceCorrector:

    def __init__(
        self,
        candidate_generator,
        evidence_providers,
        decision_engine
    ):

        self.candidate_generator = candidate_generator
        self.evidence_providers = evidence_providers
        self.decision_engine = decision_engine


    def correct(
        self,
        line,
        paragraph=None
    ):

        candidates = self.candidate_generator.generate(
            line,
            paragraph
        )

        best_candidate = self._select_best(
            candidates
        )

        if best_candidate:
            return best_candidate.candidate_text

        return line.text


    def _select_best(
        self,
        candidates
    ):

        if not candidates:
            return None

        for candidate in candidates:

            for provider in self.evidence_providers:

                score = provider.score(candidate)

                if provider.name == "geometry":
                    candidate.geometry_score = score

                elif provider.name == "lexical":
                    candidate.lexical_score = score

                elif provider.name == "context":
                    candidate.context_score = score

            self.decision_engine.evaluate(candidate)

        return max(
            candidates,
            key=lambda c: c.final_score
        )