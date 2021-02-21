
# Universal sentence encoder
import numpy as np
import tensorflow_hub as hub

class Semantic_Comparator():

    def __init__(self, sentences):
        self.embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        self.embeddings = self.embed(sentences)

    def get_semantic_similarity(self):
        return np.inner(self.embeddings, self.embeddings)