
# Ask 2 types of questions:
#       1. Fill in the blank --> use spaCy NLP to find "keywords" to remove
#       2. What/When/Where --> use intent extraction and sentence similarity to compare answers

from spacy_nn import Spacy_NN
from uni_sen_encoder import Semantic_Comparator

class Question_Handler():

    def __init__(self, highlights):
        self.highlights = highlights
        

    def check_answers(self, response):
        if len(self.www_q) == 0:
            return "no question generated"
        else:
            self.semantic_comparator = Semantic_Comparator([self.www_q, response])
            return semantic_comparator.get_semantic_similarity()