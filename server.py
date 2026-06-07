from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/log')
def log():
    try:
        with open('log.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ''

if __name__ == '__main__':
    app.run(port=5000)