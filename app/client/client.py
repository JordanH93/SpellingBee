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
        score = 0
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
        response = stub.getWord(spelling_bee_pb2.GetWord(get_word=self))
        return response


# Using 150 line breaks instead of clear because cls does not work on some IDEs
def clear():
    print('\n' * 150)


def select_difficulty():
    while True:
        try:
            clear()
            print(BANNER)
            choice = int(input(WELCOME))
            if choice == 1:
                return choice
            elif choice == 2:
                return choice
            elif choice == 3:
                return choice
            else:
                print("Please choose a valid difficulty")
        except:
            print("Please enter a valid option.")


if __name__ == "__main__":
    Client.run()
