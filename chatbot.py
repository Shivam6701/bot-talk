from chatterbot_lib import Chatterbot_mod
from pyttsx3_lib import Pyttsx3_mod

class Bot:
    def __init__(self):
        super().__init__()

        self.c_m = Chatterbot_mod()
        self.p_m = Pyttsx3_mod()

    def question(self,qu):

        print("press q to quit")
        print("\n Start your conversation \n")
        while True:

            ques = qu
            if ques != 'q':
                answer = self.c_m.respond(ques)
                print(answer)
                return answer
                #self.p_m.voice(answer)


            else:

                #self.p_m.voice("Thank you, Have a good day")
                return "Thank you"
                #break





