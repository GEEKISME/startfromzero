# 下面是 Flask 版 hello world 的构建过程。
from flask import Flask


App = Flask(__name__)
@App.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    App.run(debug=True)