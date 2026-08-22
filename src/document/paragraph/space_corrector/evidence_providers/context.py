class ContextProvider:

    def __init__(self, language_model):

        self.language_model = language_model


    def score(self, candidate):

        if candidate.paragraph is None:
            return 0.0


        context = self._build_context(
            candidate
        )

        return self.language_model.score(
            context,
            candidate.candidate_text
        )


    def _build_context(self, candidate):

        paragraph = candidate.paragraph

        return paragraph.text