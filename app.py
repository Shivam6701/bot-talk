from flask import Flask , render_template, request
from chatbot import Bot
import os
import waitress

if __name__ == '__main__':
    b1 = Bot()



    app = Flask(__name__)


    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/', methods = ['POST'])
    def abou():
        ques = request.form['box']
        answer = b1.question(ques)

        return render_template('index.html', out = answer)



    app.run()
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)
