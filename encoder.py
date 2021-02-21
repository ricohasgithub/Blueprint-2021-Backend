
# Universal sentence encoder
import tensorflow_hub as hub

class Universal_Sentence_Encoder():

    def __init__(self, sentences):
        embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        embeddings = embed([
            "The quick brown fox jumps over the lazy dog.",
            "I am a sentence for which I would like to get its embedding"])

    def get_semantic_similarity(self, labels, features, rotation):
        corr = np.inner(features, features)