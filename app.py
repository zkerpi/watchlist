from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

# @app.route('/user/<name>')
# def hello(name):
#     image_path = url_for('static', filename='totoro.gif')
#     return f'<h1>Hello {escape(name)}</h1><img src="{image_path}" alt="Totoro">'

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
    {'title': '名侦探柯南', 'year': '2023'},
]

@app.route('/')
def index():
    # render_template函数可以把模板渲染出来，必须传入的参数为模板文件名（相对于template根目录的文件路径），为了让模板
    # 正确渲染，还需要把模板内部使用的变量通过关键字参数传入这个函数
    return render_template('index.html', name=name, movies=movies)
