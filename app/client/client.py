import spelling_bee_pb2
import spelling_bee_pb2_grpc
import grpc

BANNER = """
███████╗██████╗ ███████╗██╗     ██╗     ██╗███╗   ██╗ ██████╗     ██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██║     ██║     ██║████╗  ██║██╔════╝     ██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝█████╗  ██║     ██║     ██║██╔██╗ ██║██║  ███╗    ██████╔╝█████╗  █████╗  
╚════██║██╔═══╝ ██╔══╝  ██║     ██║     ██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══╝  ██╔══╝  
███████║██║     ███████╗███████╗███████╗██║██║ ╚████║╚██████╔╝    ██████╔╝███████╗███████╗
╚══════╝╚═╝     ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚══════╝╚══════╝
"""
DIFFICULTY = """
        Please choose a difficulty to begin playing:
        .1) Easy
        .2) Moderate
        .3) Difficult
"""
WELCOME = """
Welcome to Spelling Bee!
        Please choose a game mode:
        .1) Single Player
        .2) Multiplayer
"""
MULTI = """
        Please choose an option:
        .1) Start game
        .2) Join game
"""

"""
1. This class will be run the game on the 'client' device
- the user selects a difficulty (Beginner, moderate, difficult)
- the client sends a request to the server for the chosen game type
- The server responds with the letters for the game, the total score, the random mandatory character and words remaining
- player score increments with each correctly entered word
- word must be greater length 4, not be used already and contain the given characters
- When all the possible word combinations are used the player is given the option to exit or play again. 

"""


class Client:
    def __init__(self):
        self.score = 0
        self.words = []
        self.show_words = False
        self.show_code = False
        self.given_chars = None
        self.rand_char = None
        self.words_remaining = 0
        self.encouragement = "Beginner"
        self.total_score = 0
        self.isMultiplayer = False
        self.name = ""
        self.invite_id = ""

    def run(self):
        if self.is_single_player():
            self.start_game()
            self.play()
        else:
            self.isMultiplayer = True
            if self.is_join_game():
                self.name = self.get_name()
                self.join_game()
            else:
                self.name = self.get_name()
                self.start_game()
                self.play()

    def join_game(self):
        print("test")

    def get_name(self):
        while True:
            self.clear()
            print(BANNER)
            choice = input("Please enter name: \n>>").lower()
            if choice.isalpha() and len(choice) > 2:
                return choice
            else:
                input("Word must contain letters only and be greater than two characters.\nPress enter to continue.")

    def start_game(self):
        difficulty = self.select_difficulty()
        self.score = self.create_game(difficulty)
        response = self.get_word(" ")
        self.words_remaining = response.remaining
        self.given_chars = set(response.word)
        self.rand_char = response.rand_char
        self.total_score = response.total
        self.invite_id = response.session_id

    def play(self):
        while True:
            self.clear()
            self.banner()
            word = self.validate_input()
            resp = self.submit_word(word)
            self.score = resp.score
            if resp.response:
                self.words.append(word)
            self.words_remaining = resp.remaining
            self.get_encouragement()
            self.check_endgame()

    def is_single_player(self):
        while True:
            try:
                self.clear()
                print(BANNER)
                choice = int(input(WELCOME))
                if choice == 1:
                    return True
                elif choice == 2:
                    return False
                else:
                    print("Please choose a valid difficulty")
            except:
                print("Please enter a valid option.")

    def is_join_game(self):
        while True:
            try:
                self.clear()
                print(BANNER)
                choice = int(input(MULTI))
                if choice == 1:
                    return False
                elif choice == 2:
                    return True
                else:
                    print("Please choose a valid difficulty")
            except:
                print("Please enter a valid option.")

    # 1. Submits our word for approval
    # - returns true / false, score & words remaining
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
    # - returns words remaining
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
                choice = int(input(DIFFICULTY))
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

    # 1. Print our game banner
    # - prints word of encouragement, score, optionally words submitted and our given letters
    def banner(self):
        if self.isMultiplayer:
            dashboard = """
            {}: {}
            Words remaining: {}
            Options: (Q)uit -- (W)ords -- (I)nvite
            """.format(self.encouragement, self.score, self.words_remaining)
        else:
            dashboard = """
            {}: {}
            Words remaining: {}
            Options: (Q)uit -- (W)ords
            """.format(self.encouragement, self.score, self.words_remaining)
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
        if self.show_code and self.isMultiplayer:
            print(f"Invite code: {self.invite_id}")

    # 1. validates the user input for their word attempt
    # - We can quit with 'q' and toggle the word list with 'w'
    # - If the word is greater than length 4, contains only given letters, contains the random character and hasn't been
    # - used then it is sent to the server
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
                    elif not self.show_words:
                        self.show_words = True
                    continue
                elif choice == 'i' and self.isMultiplayer:
                    if self.show_code:
                        self.show_code = False
                    elif not self.show_code:
                        self.show_code = True
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
            else:
                input("Word must contain letters only.\nPress enter to continue.")

    # 1. calculates our score as a percentage of the total possible score.
    # - prints a message depending on the score percent
    def get_encouragement(self):
        if ((self.score / self.total_score) * 100) < 3:
            self.encouragement = "Beginner"
        elif ((self.score / self.total_score) * 100) < 7:
            self.encouragement = "Good Start"
        elif ((self.score / self.total_score) * 100) < 11:
            self.encouragement = "Moving Up"
        elif ((self.score / self.total_score) * 100) < 20:
            self.encouragement = "Good"
        elif ((self.score / self.total_score) * 100) < 33:
            self.encouragement = "Solid"
        elif ((self.score / self.total_score) * 100) < 53:
            self.encouragement = "Nice"
        elif ((self.score / self.total_score) * 100) < 67:
            self.encouragement = "Great"
        elif ((self.score / self.total_score) * 100) < 93:
            self.encouragement = "Amazing"
        else:
            self.encouragement = "Genius"

    # 1. Checks if all given letter combinations have been used and ends or starts a new game per user choice
    def check_endgame(self):
        if self.words_remaining == 0:
            while True:
                self.clear()
                print(BANNER)
                choice = input("Congratulations! You win.\nNew game? (y/n)").lower()
                if choice == 'y':
                    self.run()
                elif choice == 'n':
                    exit()
                else:
                    input("Please enter 'y' for yes or 'n' for no\nPress enter to continue.")

    # 1. prints our valid submitted words
    def print_word_list(self):
        print("Words list:")
        for i in self.words:
            print(i)


if __name__ == "__main__":
    Client().run()
