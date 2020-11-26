from flask import Flask, render_template, request
from chatbot import Bot

app = Flask(__name__)


b1 = Bot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', method=['POST','GET'])
def abou():
    ques = request.form['box']
    answer = b1.question(ques)
    return render_template('index.html', out=answer)
if __name__ == '__main__':
    app.run()
