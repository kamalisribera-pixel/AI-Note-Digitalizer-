from transformers import AutoTokenizer, AutoModel

class DebertaLoader:
    MODEL_NAME ="microsoft/deberta-v3-base"

    def __init__(self):
        self._tokenizer = None
        self._model = None

    def load(self):
        if self._tokenizer is None:
            self._tokenizer = AutoTokenizer.from_pretrained(self.MODEL_NAME)
        if self._model is None:
            self._model = AutoModel.from_pretrained(self.MODEL_NAME)
        return(self._tokenizer, self._model)