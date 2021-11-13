from concurrent import futures
import grpc
import spelling_bee_pb2
import spelling_bee_pb2_grpc
from app.server import connections
from app.server import spelling_bee_factory
from app.server import create_dictionary
from random import randint


class Listener(spelling_bee_pb2_grpc.SpellingBeeServiceServicer):
    def __init__(self):
        self.connection = connections.Connection
        self.dictionary = self.connection.get_dictionary_json()
        self.game = None
        self.pangram_dict = None
        self.score = 0
        self.current_pangram = ""
        self.random_char = ""
        self.current_pangram_subset_dict = {}
        self.words_remaining = 0

    def setWord(self, request, context):
        is_valid_word = False
        if request.set_word in self.current_pangram_subset_dict:
            is_valid_word = True
            self.calculate_score(request.set_word)
            del self.current_pangram_subset_dict[request.set_word]
        words_remaining = len(self.current_pangram_subset_dict.keys())
        print("app.server.server.setWord: Chosen Pangram = {}".format(self.current_pangram))
        print("app.server.server.setWord: Words remaining = {}".format(self.words_remaining))
        print("app.server.server.setWord: Possible words = {}".format(self.current_pangram_subset_dict))
        return spelling_bee_pb2.Response(response=is_valid_word, score=self.score, remaining=words_remaining)

    def createGame(self, request, context):
        # game_choice = 1
        self.score = 0  # remove this if keeping a persistent score between games
        self.game = spelling_bee_factory.SpellingBeeFactory().build_game(request.selection)
        self.pangram_dict = create_dictionary.CreateDictionary(self.game.word_length,
                                                               self.dictionary)  # might be better to be contained within the factory subclasses
        # word = generate_word(self.pangram_dict.pangrams)
        return spelling_bee_pb2.Game(score=self.score)

    def getWord(self, request, context):
        word = self.generate_word(self.pangram_dict.pangrams)
        print("app.server.server.getWord: Chosen Pangram = {}".format(self.current_pangram))
        print("app.server.server.getWord: Words remaining = {}".format(self.words_remaining))
        print("app.server.server.getWord: Possible words = {}".format(self.current_pangram_subset_dict))
        return spelling_bee_pb2.Word(word=word, rand_char=self.random_char, remaining=self.words_remaining)

    def generate_word(self, pangrams_dict):
        rand_num = randint(0, len(pangrams_dict))
        self.current_pangram = list(pangrams_dict.keys())[rand_num]
        self.random_char = "".join(set(self.current_pangram[randint(0, len(self.current_pangram))]))
        word = "".join(set(self.current_pangram))
        self.get_pangram_subsets(self.dictionary)
        self.words_remaining = len(self.current_pangram_subset_dict.keys())
        #print(self.words_remaining)

        # print(self.current_pangram)
        return word

    # 1. Class creates another dictionary of subsets of our pangram as a set
    # - The new dictionary will only contain words greater or equal to length 4
    # - words will also contain our random character
    # - We are also excluding words that are the same char example: 'mmmm'
    def get_pangram_subsets(self, dictionary):
        for word in dictionary:
            if set(word).issubset(set(self.current_pangram)) and len(word) >= 4 and self.random_char in word:
                if word != len(word) * word[0]:
                    self.current_pangram_subset_dict[word] = ""

    def calculate_score(self, word):
        if len(word) == 4:
            self.score += 1
        elif set(word) == set(self.current_pangram):
            self.score += len(word) + 7
        else:
            self.score += len(word)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    spelling_bee_pb2_grpc.add_SpellingBeeServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
