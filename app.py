import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'
@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
