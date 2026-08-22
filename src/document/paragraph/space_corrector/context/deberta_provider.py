import torch

from .deberta_loader import DebertaLoader

import torch.nn.functional as F

class DebertaProvider:

    name = "context"


    def __init__(self):

        loader = DebertaLoader()

        self.tokenizer, self.model = loader.load()

        self.model.eval()


    def score(
        self,
        candidate
    ):

        with torch.no_grad():

            inputs = self.tokenizer(
                candidate.candidate_text,
                return_tensors="pt",
                truncation=True,
                max_length=512
            )

            outputs = self.model(**inputs)

            embedding = outputs.last_hidden_state[:, 0, :]
            candidate_embedding = self._embed(
                candidate.candidate_text
            )

            original_embedding = self._embed(
                candidate.original_line.text
            )

            similarity = F.cosine_similarity(
                candidate_embedding,
                original_embedding
            )

            score = similarity.item()

            return (score + 1) / 2

        return 0.5
    def _embed(self, text):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():

            outputs = self.model(**inputs)

            embedding = outputs.last_hidden_state[:, 0, :]

        return embedding