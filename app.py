from flask import Flask, jsonify
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
    print("list student printing")
    data = {"message" : "app is running"}
    return jsonify(data), 200


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)