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

    def setWord(self, request, context):
        is_valid_word = False
        score = 5
        if request.set_word == "client":
            is_valid_word = True
        return spelling_bee_pb2.Response(response=is_valid_word, score=score)

    def createGame(self, request, context):
        # game_choice = 1
        self.score = 0  # remove this if keeping a persistent score between games
        self.game = spelling_bee_factory.SpellingBeeFactory().build_game(request.selection)
        self.pangram_dict = create_dictionary.CreateDictionary(self.game.word_length,
                                                               self.dictionary)  # might be better to be contained within the factory subclasses
        # word = generate_word(self.pangram_dict.pangrams)
        return spelling_bee_pb2.Game(score=self.score)

    def getWord(self, request, context):
        word, rand_char = generate_word(self.pangram_dict.pangrams)
        return spelling_bee_pb2.Word(word=word, rand_char=rand_char)


def generate_word(self):
    rand_num = randint(0, len(self))
    random_pangram = list(self.keys())[rand_num]
    rand_char = "".join(set(random_pangram[randint(0, len(random_pangram))]))
    word = "".join(set(random_pangram))
    print("app.server.server.generate_word: Chosen Pangram = {}".format(random_pangram))
    return word, rand_char


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    spelling_bee_pb2_grpc.add_SpellingBeeServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
