from flask import Flask, request, jsonify
from cs50 import SQL
from flask_cors import CORS, cross_origin
import json

from models.question_handler import Question_Handler

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#config db
db = SQL("sqlite:///quiz.db")

@app.route('/', methods=['POST'])
def ml_func():
    if request.method == "POST":
        text = json.loads(request.data)
        text = text['data']
        text = text.replace('\n','')
        text = text.replace('\xa0','')
        text = text.replace('\t','')
        text = text.replace('\r','')
    textList = text.split(".")  
    # CALL ML
    print(textList)
    hiqs_handler = Question_Handler(textList)

    questions = hiqs_handler.generate_list_fitb()
    frq_questions = hiqs_handler.generate_frq()
    print(frq_questions)

    # Both questions and answers together
    responses = []
    qs = []
    answers = []

    qs.append(frq_questions["question"])
    answers.append(frq_questions["answer"])

    for q in questions:
        qs.append(q["question"])
        answers.append(q["answer"])
    
    for i in range(len(qs)):
        db.execute("INSERT INTO quiz (question, answer) VALUES (:question, :answer)", question=qs[i], answer=answers[i])

    # SAVE TO DB
    return "hello"

@app.route('/getQs', methods=['GET'])
def sendInfo():
    # return all questions and responses
    quizes = db.execute("SELECT * FROM quiz")
    questions = []
    answers = []
    total = []
    for q in quizes:
        questions.append(q["question"])
        answers.append(q["answer"])
    total.append(questions)
    total.append(answers)
    # total = [["q1", "q2"], ["a1", "a2"]]
    return jsonify({'data' : total})

@app.route('/save')
def save_db():
    # save term and answer to db
    question = "blank"
    answer = "blank"
    db.execute("INSERT INTO quiz (question, answer) VALUES (:question, :answer)", question=question, answer=answer)
    return

if __name__ == '__main__':
    app.run(debug=True)