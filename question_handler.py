
# Ask 2 types of questions:
#       1. Fill in the blank --> use spaCy NLP to find "keywords" to remove
#       2. What/When/Where --> use intent extraction and sentence similarity to compare answers

import random

from spacy_nn import Spacy_Entity_Extractor
from uni_sen_encoder import Semantic_Comparator
from question_generator import Question_Generator

class Question_Handler():

    def __init__(self, highlights):
        self.highlights = highlights
        self.entity_extractor = Spacy_Entity_Extractor(highlights)

    def generate_fitb(self):
        nouns = self.entity_extractor.get_nouns()
        blank_noun = nouns[random.randint(0, len(nouns))]
        fitb_q1 = self.highlights[0][:self.highlights.find(blank_noun)]
        fitb_q2 = self.highlights[0][(self.highlights.find(blank_noun) + len(blank_noun)) + 1:]
        return {
            "blank": blank_noun,
            "question_b1": fitb_q1,
            "question_b2": fitb_q2
        }

    def generate_list_fitb(self):
        pass

    # I've done too many ap tests lmaoo
    def generate_frq(self):
        sentence = highlights[0]
        self.question_gen = Question_Generator(sentence)
        return {
            "question": self.question_gen.get_question()
        }

    def check_answers(self, response):
        if len(self.www_q) == 0:
            return "no question generated"
        else:
            self.semantic_comparator = Semantic_Comparator([self.www_q, response])
            return semantic_comparator.get_semantic_similarity()