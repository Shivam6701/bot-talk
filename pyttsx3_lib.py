import pyttsx3

class Pyttsx3_mod:
    def __init__(self):
        self.engine = pyttsx3.init()
        super().__init__()

    def voice(self,inpu):
        self.engine.say(inpu)
        self.engine.runAndWait()
