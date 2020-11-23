from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chatterbot_mod:

    def __init__(self):
        super().__init__()
        self.name()
        self.training()


    def name(self):

        self.chatbot = ChatBot(
            'Shivam',
            logic_adapters=[
                "chatterbot.logic.BestMatch",
                "chatterbot.logic.MathematicalEvaluation",


            ]

        )


    def training(self):
        trainer = ChatterBotCorpusTrainer(self.chatbot)

        trainer.train(
            "chatterbot.corpus.english"
        )

        conv1 = [
            "hi",
            "hello",
            "how are you",
            "Whats my name",
            "Shivam kumar",
            "how, are you shivam",
            "i'm good",

        ]
        conv2 = [
            "hi",
            "hello",
            "how are you",
            "i'm good",

        ]

        trainer = ListTrainer(self.chatbot)
        trainer.train(conv1)
        trainer.train(conv2)


    def respond(self,ques):

        response = self.chatbot.get_response(ques)
        return response
