from flask import Flask, request, jsonify
from cs50 import SQL


app = Flask(__name__)

#config db
db = SQL("sqlite:///quiz.db")

@app.route('/')
def ml_func():
    # call to ml should go here
    resp = False
    # should save actually go after ml call?
    return jsonify({'data' : resp})

@app.route('/save')
def save_db():
    # save term and answer to db
    term = "blank"
    answer = "blank"
    db.execute("INSERT INTO quiz (term, answer) VALUES (:term, :answer)", term=term, answer=answer)
    return

if __name__ == '__main__':
    app.run()