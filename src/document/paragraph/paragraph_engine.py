from src.document.paragraph.sentence_reconstructor import SentenceReconstruction


class ParagraphEngine:

    def __init__(
        self,
        space_corrector
    ):

        self.space_corrector = space_corrector

        self.reconstructor = (
            SentenceReconstruction()
        )


    def process(
        self,
        paragraph
    ):

        corrected_lines = []


        for line in paragraph.lines:

            corrected_line = (
                self.space_corrector.correct(
                    line,
                    paragraph
                )
            )

            corrected_lines.append(
                corrected_line
            )


        return self.reconstructor.reconstruct(
            corrected_lines
        )