from flask import Flask

app = Flask(__name__)


@app.get('/welcome')
def welcome():
    """ returns welcome"""
    return "welcome"


@app.get('/welcome/home')
def welcome_home():
    """ returns welcome home"""
    return "welcome home"


@app.get('/welcome/back')
def welcome_back():
    """ returns welcome back"""
    return "welcome back"
