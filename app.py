from flask import Flask , render_template, request
from chatbot import Bot

app = Flask(__name__)

if __name__ == '__main__':
    b1 = Bot()

    

    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/', methods = ['POST','GET'])
    def abou():
        ques = request.form['box']
        answer = b1.question(ques)

        return render_template('index.html', out = answer)

    app.run()
   
