
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

class Spacy_NN():

    def __init__(self, text):
        # Process whole documents
        self.text_in = text
        self.doc = nlp(self.text_in)
        self.nouns = [chunk.text for chunk in self.doc.noun_chunks]
        self.verbs = [token.lemma_ for token in self.doc if token.pos_ == "VERB"]

    def get_nouns(self):
        return nouns

    def get_verbs(self):
        return verbs

    def print_lem(self):
        for entity in self.doc.ents:
            print(entity.text, entity.label_)