from flask import Flask, request, jsonify
from cs50 import SQL


app = Flask(__name__)


@app.route('/')
def ml_func():
    # call to ml should go here
    resp = False
    return jsonify({'data' : resp})

@app.route('/save')
def save_db():
    # call to ml should go here
    resp = False
    return jsonify({'data' : resp})

if __name__ == '__main__':
    app.run()