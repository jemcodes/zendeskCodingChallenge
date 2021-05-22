import requests
import base64
from flask import Flask, render_template
from .config import Configuration

app = Flask(__name__)

email = Configuration.email
password = Configuration.password
encoded_data = base64.b64encode(
    bytes(f'{email}:{password}', 'utf-8')).decode('utf-8')
auth_header = f'Basic {encoded_data}'


@app.route('/')
def hello_world():
    """Send a test message to the browser"""
    return jsonify({'message': 'hello world!'})


if __name__ == '__main__':
    app.run(debug=True)
