from flask import Flask, request, jsonify
from cs50 import SQL
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#config db
db = SQL("sqlite:///quiz.db")

@app.route('/', methods=['POST'])
def ml_func():
    if request.method == "POST":
        print("run")
        text = json.loads(request.data)
        text = text['data']
        # text = request.json['data']
    # call to ml should go here
    print(text)
    resp = "SUCCESS!"
    # should save actually go after ml call?
    return jsonify({'data' : resp})

@app.route('/g', methods=['GET'])
def get():
    resp = "SUCCESS!"
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
    app.run(debug=True)