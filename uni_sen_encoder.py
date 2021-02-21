
# Universal sentence encoder via transfer learning
import numpy as np
import tensorflow_hub as hub

class Semantic_Comparator():

    def __init__(self, sentences):
        self.embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        self.embeddings = self.embed(sentences)

    def get_semantic_similarity(self):
        # The semantic similarity between 2 embedded texts is the inner products of their encodings
        return np.inner(self.embeddings, self.embeddings)