from spacy_nn import Spacy_Entity_Extractor
from uni_sen_encoder import Semantic_Comparator
from question_handler import Question_Handler
from question_generator import Question_Generator

extext = "42 is the answer to life, universe and everything."
q_gen = Question_Generator(extext)
print(q_gen.get_question())
print(q_gen.get_answer())

q_handler = Question_Handler("When Sebastian Thrun started working on self-driving cars, few people took him seriously.")
print(q_handler.generate_fitb())

'''
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

nn = Spacy_Entity_Extractor(text)
nn.print_lem()

use = Semantic_Comparator([
            "I like my phone",
            "Hello my name is Rico."])

print(use.get_semantic_similarity())

'''