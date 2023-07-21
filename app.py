from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<name>')
def hello(name):
    image_path = url_for('static', filename='totoro.gif')
    return f'<h1>Hello {escape(name)}</h1><img src="{image_path}" alt="Totoro">'