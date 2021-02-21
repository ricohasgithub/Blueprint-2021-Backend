from spacy_nn import Spacy_Entity_Extractor
from uni_sen_encoder import Semantic_Comparator

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

