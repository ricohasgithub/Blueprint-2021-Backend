
# Ask 2 types of questions:
#       1. Fill in the blank --> use spaCy NLP to find "keywords" to remove
#       2. What/When/Where --> use intent extraction and sentence similarity to compare answers

from spacy_nn import Spacy_Entity_Extractor
from uni_sen_encoder import Semantic_Comparator

class Question_Handler():

    def __init__(self, highlights):
        self.highlights = highlights
        self.entity_extractor = Spacy_Entity_Extractor(highlights)

    def generate_fitb(self):
        nouns = self.entity_extractor.get_nouns()
        blank_noun = nouns[0]
        fitb_q1 = self.highlights[:self.highlights.find(blank_noun)]
        fitb_q2 = self.highlights[(self.highlights.find(blank_noun) + len(blank_noun)) + 1:]
        return {
            "blank": blank_noun,
            "fitb_q1": fitb_q1,
            "fitb_q2": fitb_q2
        }

    def check_answers(self, response):
        if len(self.www_q) == 0:
            return "no question generated"
        else:
            self.semantic_comparator = Semantic_Comparator([self.www_q, response])
            return semantic_comparator.get_semantic_similarity()