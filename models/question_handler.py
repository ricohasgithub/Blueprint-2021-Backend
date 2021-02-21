
# Ask 2 types of questions:
#       1. Fill in the blank --> use spaCy NLP to find "keywords" to remove
#       2. What/When/Where --> use intent extraction and sentence similarity to compare answers

import random

from models.spacy_nn import Spacy_Entity_Extractor
from models.uni_sen_encoder import Semantic_Comparator
from models.question_generator import Question_Generator

class Question_Handler():

    def __init__(self, highlights):
        self.highlights = highlights
        self.entity_extractor = []
        for sentence in highlights:
            self.entity_extractor.append(Spacy_Entity_Extractor(sentence))

    def generate_fitb(self):
        rand_sentence_seed = random.randint(0, len(self.highlights))
        nouns = self.entity_extractor[rand_sentence_seed].get_nouns()
        blank_noun = nouns[random.randint(0, len(nouns) - 1)]
        fitb_q1 = self.highlights[rand_sentence_seed][:self.highlights[rand_sentence_seed].find(blank_noun)]
        fitb_q2 = self.highlights[rand_sentence_seed][(self.highlights[rand_sentence_seed].find(blank_noun) + len(blank_noun)) + 1:]
        return {
            "type": "fitb",
            "answer": blank_noun,
            "question": fitb_q1 + "____" + fitb_q2
        }

    def generate_fitb_from_seed(self, rand_sentence_seed):
        nouns = self.entity_extractor[rand_sentence_seed].get_nouns()
        blank_noun = nouns[random.randint(0, len(nouns) - 1)]
        fitb_q1 = self.highlights[rand_sentence_seed][:self.highlights[rand_sentence_seed].find(blank_noun)]
        fitb_q2 = self.highlights[rand_sentence_seed][(self.highlights[rand_sentence_seed].find(blank_noun) + len(blank_noun)) + 1:]
        return {
            "type": "fitb",
            "answer": blank_noun,
            "question": fitb_q1 + "____" + fitb_q2
        }

    def generate_list_fitb(self):
        random_sentence_seeds = random.sample(range(0, len(self.highlights)), 3)
        fitb_questions = []
        for seed in random_sentence_seeds:
            fitb_questions.append(self.generate_fitb_from_seed(seed))
        return fitb_questions

    # I've done too many ap tests lmaoo
    def generate_frq(self):
        sentence = self.highlights[0]
        self.www_q = Question_Generator(sentence)
        return {
            "type": "frq",
            "question": self.www_q.get_question(),
            "answer": self.www_q.get_answer()
        }

    # def check_answers(self, response):
    #     self.semantic_comparator = Semantic_Comparator([self.www_q.get_answer(), response])
    #     return semantic_comparator.get_semantic_similarity()