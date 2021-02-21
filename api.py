from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def ml_func():
    return "Hello World!"

if __name__ == '__main__':
    app.run()