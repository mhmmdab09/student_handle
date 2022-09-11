from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    '''main page'''
    return("hello")


@app.route('/v1/sigup_student')
def signup_student():
    pass


@app.route('/v1/renew_student')
def renew_student():
    pass


@app.route('/v1/use_session')
def use_session():
    pass


@app.route('/v1/list_students')
def list_students():
    return("is working")


