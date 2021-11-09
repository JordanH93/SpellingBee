import spelling_bee_pb2
import spelling_bee_pb2_grpc
import grpc


def run():
    client_word = "client"
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
        response = stub.getWord(spelling_bee_pb2.GetWord(get_word=client_word))
        print("response: %s" % response.rec_word)


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()
