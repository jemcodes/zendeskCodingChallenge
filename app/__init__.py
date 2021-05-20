import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Send a test message to the browser"""
    return jsonify({'message': 'hello world!'})


if __name__ == '__main__':
    app.run(debug=True)
