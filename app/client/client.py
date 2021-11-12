import spelling_bee_pb2
import spelling_bee_pb2_grpc
import grpc
from app.client import validation
import os

BANNER = """
███████╗██████╗ ███████╗██╗     ██╗     ██╗███╗   ██╗ ██████╗     ██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██║     ██║     ██║████╗  ██║██╔════╝     ██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝█████╗  ██║     ██║     ██║██╔██╗ ██║██║  ███╗    ██████╔╝█████╗  █████╗  
╚════██║██╔═══╝ ██╔══╝  ██║     ██║     ██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══╝  ██╔══╝  
███████║██║     ███████╗███████╗███████╗██║██║ ╚████║╚██████╔╝    ██████╔╝███████╗███████╗
╚══════╝╚═╝     ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚══════╝╚══════╝
"""
WELCOME = """
Welcome to Spelling Bee!
        Please choose a difficulty to begin playing:
        .1) Easy
        .2) Moderate
        .3) Difficult
"""


class Client:
    def __init__(self):
        #self.validate = validation.Validate()
        self.score = 0
        self.words = []
        self.show_words = False
        self.given_chars = None
        self.rand_char = None

    def run(self):
        difficulty = self.select_difficulty()
        self.score = self.create_game(difficulty)
        response = self.get_word(" ")
        #response = set(self.get_word(" "))
        self.given_chars = set(response.word)
        self.rand_char = response.rand_char
        #print(self.rand_char)

        while True:
            self.clear()
            self.banner()

            word = self.validate_input()
            resp = self.submit_word(word)
            print(resp.response)
            break

    # 1. Submits our word for approval
    # - returns true / false
    # - returns score
    def submit_word(self, word):
        with grpc.insecure_channel("localhost:9999") as channel:
            stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
            response = stub.setWord(spelling_bee_pb2.SetWord(set_word=word))
            return response

    # 1. Create our game
    # - Sets the word length
    def create_game(self, difficulty):
        with grpc.insecure_channel("localhost:9999") as channel:
            stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
            response = stub.createGame(spelling_bee_pb2.GetGame(selection=difficulty))
            return response.score

    # 1. Get a word to start playing the game
    # - Gets a word of length determined by game difficulty
    def get_word(self, empty_string):
        with grpc.insecure_channel("localhost:9999") as channel:
            stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
            response = stub.getWord(spelling_bee_pb2.GetWord(request=empty_string))
            return response

    # 1. Using 150 line breaks instead of clear because cls does not work on some IDEs
    # - Can turn off if too annoying
    def clear(self):
        clr = True
        if clr:
            print('\n' * 150)

    # 1. Select the difficulty of our game
    def select_difficulty(self):
        while True:
            try:
                self.clear()
                print(BANNER)
                choice = int(input(WELCOME))
                if choice == 1:
                    return "Easy"
                elif choice == 2:
                    return "Moderate"
                elif choice == 3:
                    return "Difficult"
                else:
                    print("Please choose a valid difficulty")
            except:
                print("Please enter a valid option.")

    def banner(self):
        dashboard = """
        Score: {}
        Options: (Q)uit -- (W)ords
        """.format(self.score)
        print(BANNER)
        letters = ""
        if self.show_words:
            self.print_word_list()
        print(dashboard)
        for i in self.given_chars:
            if i == self.rand_char:
                letters += "[{}]".format(i)
            else:
                letters += i
        print("Letters: {}".format(letters))

    def validate_input(self):
        while True:
            self.clear()
            self.banner()
            choice = input(">> ").lower()
            if choice.isalpha():
                if choice == 'q':
                    print("Thank you for playing!")
                    exit()
                elif choice == 'w':
                    if self.show_words:
                        self.show_words = False
                    if not self.show_words:
                        self.show_words = True
                    continue
                elif len(choice) < 4:
                    input("Word must be more than 4 characters\nPress enter to continue.")
                    continue
                elif not set(choice).issubset(self.given_chars):
                    input("Word must contain only given characters\nPress enter to continue.")
                    continue
                elif choice in self.words:
                    input("Word must not have already been used.\nPress enter to continue.")
                    continue
                elif self.rand_char not in choice:
                    input("Word must contain '{}'.\nPress enter to continue.".format(self.rand_char))
                    continue
                else:
                    return choice


    def print_word_list(self):
        for i in self.words:
            print(i)



if __name__ == "__main__":
    Client().run()
