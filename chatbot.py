from chatterbot_lib import Chatterbot_mod

class Bot:
    def __init__(self):
        super().__init__()

        self.c_m = Chatterbot_mod()
        

    def question(self,qu):

        print("press q to quit")
        print("\n Start your conversation \n")
        while True:

            ques = qu
            if ques != 'q':
                answer = self.c_m.respond(ques)
                print(answer)
                return answer
               
            else:
                return "Thank you"
                
