from flask import Flask, render_template
application = Flask(__name__)
app = application


@application.route('/')
def hello_world():
    return render_template('home.html')
