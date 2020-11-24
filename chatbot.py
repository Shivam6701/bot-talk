from chatterbot_lib import Chatterbot_mod

class Bot:

    def __init__(self):
        super().__init__()

        self.c_m = Chatterbot_mod()

    def question(self, qu):
        while True:

            ques = qu
            try:
                answer = self.c_m.respond(ques)

                return answer
            except:
                return "Thank you"
