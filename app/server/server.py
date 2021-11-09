from concurrent import futures
import grpc
import spelling_bee_pb2
import spelling_bee_pb2_grpc


class Listener(spelling_bee_pb2_grpc.SpellingBeeServiceServicer):

    def getWord(self, request, context):
        server_word = "word false"
        if request.get_word == "client":
            server_word = "Word true"

        return spelling_bee_pb2.ReceiveWord(rec_word=server_word)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    spelling_bee_pb2_grpc.add_SpellingBeeServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
