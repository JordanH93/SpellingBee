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

    def getWord(self, request, context):
        is_valid_word = False
        score = 5
        if request.get_word == "client":
            is_valid_word = True
        return spelling_bee_pb2.Response(response=is_valid_word, score=score)

    def createGame(self, request, context):
        # game_choice = 1
        self.game = spelling_bee_factory.SpellingBeeFactory().build_game(request.selection)
        self.pangram_dict = create_dictionary.CreateDictionary(self.game.word_length, self.dictionary)
        word = generate_word(self.pangram_dict.pangrams)
        return spelling_bee_pb2.Game(set_word=word)
        # game code here


def generate_word(self):
    rand_num = randint(0, len(self.pangram_dict))
    random_pangram = list(self.pangram_dict.keys())[rand_num]
    return random_pangram


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    spelling_bee_pb2_grpc.add_SpellingBeeServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
