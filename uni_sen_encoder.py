
# Universal sentence encoder
import tensorflow_hub as hub

class Semantic_Comparator():

    def __init__(self, sentences):
        self.embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        self.embeddings = self.embed([
            "The quick brown fox jumps over the lazy dog.",
            "I am a sentence for which I would like to get its embedding"])

    def get_semantic_similarity(self):
        return np.inner(self.embeddings, self.embeddings)