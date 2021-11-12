import spelling_bee_pb2
import spelling_bee_pb2_grpc
import grpc
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

    @staticmethod
    def run():
        difficulty = select_difficulty()
        score = create_game(difficulty)
        while True:
            clear()
            print(BANNER)
            print("Score: {} ".format(score))
            word = input(">>")
            resp = submit_word(word)
            print(resp.response)
            break


# Submits our word for approval
# - returns true / false
# - returns score
def submit_word(self):
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
        response = stub.setWord(spelling_bee_pb2.SetWord(set_word=self))
        return response


def create_game(self):
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
        response = stub.createGame(spelling_bee_pb2.GetGame(selection=self))
        return response.score


# Using 150 line breaks instead of clear because cls does not work on some IDEs
# - Can turn off if too annoying
def clear():
    clr = True
    if clr:
        print('\n' * 150)


def select_difficulty():
    while True:
        try:
            clear()
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


if __name__ == "__main__":
    Client.run()
