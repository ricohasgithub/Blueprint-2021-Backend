
# Context based question generator from SQUAD dataset and Seq2Seq NN
from question_gen.pipelines import pipeline

class Question_Generator():

    def __init__(self, text):
        self.text = text
        self.q_pipeline = pipeline("question-generation")
        self.prediction = self.q_pipeline(text)
    
    def get_question(self):
        return self.prediction[0]["question"]

    def get_answer(self):
        return self.prediction[0]["answer"]