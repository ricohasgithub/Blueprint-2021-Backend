
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
        sns.set(font_scale=1.2)
        g = sns.heatmap(
            corr,
            xticklabels=labels,
            yticklabels=labels,
            vmin=0,
            vmax=1,
            cmap="YlOrRd")
        g.set_xticklabels(labels, rotation=rotation)
        g.set_title("Semantic Textual Similarity")