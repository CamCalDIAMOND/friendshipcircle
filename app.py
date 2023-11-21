from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Custom working from logan!'