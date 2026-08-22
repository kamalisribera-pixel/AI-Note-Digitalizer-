from wordfreq import top_n_list

from .vocabulary import Vocabulary



class VocabularyLoader:


    def load_english(
        self,
        size=50000
    ):
        
        words = top_n_list(
            "en",
            size
        )

        return Vocabulary(
            words
        )