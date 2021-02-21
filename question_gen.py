
# Ask 3 types of questions:
#       1. Fill in the blank --> use spaCy NLP to find "keywords" to remove
#       2. What/When/Where --> use intent extraction and sentence similarity to compare answers
#       3. 

from spacy_nn import Spacy_NN

class Question_Generator():

    def __init__(self, highlights):
        self.highlights = highlights