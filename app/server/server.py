from concurrent import futures
import grpc
import spelling_bee_pb2
import spelling_bee_pb2_grpc
from app.server import connections


class Listener(spelling_bee_pb2_grpc.SpellingBeeServiceServicer):

    def getWord(self, request, context):
        is_valid_word = False
        score = 5
        if request.get_word == "client":
            is_valid_word = True

        return spelling_bee_pb2.Response(response=is_valid_word, score=score)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    spelling_bee_pb2_grpc.add_SpellingBeeServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    server.wait_for_termination()


class Run:
    def __init__(self):
        self.connection = connections.Connection
        self.dictionary = self.connection.get_dictionary_json()


if __name__ == "__main__":
    serve()