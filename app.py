import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title='Home')


@app.route('/register')
def register():
    return render_template('register.html', page_title='Register')


@app.route('/login')
def login():
    return render_template('login.html', page_title='Login')


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)