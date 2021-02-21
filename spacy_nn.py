
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

class spacy_nn():

    def __init__(self, text):
        # Process whole documents
        self.text = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")
        self.doc = nlp(text)
        self.nouns = [chunk.text for chunk in doc.noun_chunks]
        self.verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]


    def get_nouns(self):
        return nouns

    def get_verbs(self):
        return verbs

    def print_lem(self):
        for entity in doc.ents:
            print(entity.text, entity.label_)