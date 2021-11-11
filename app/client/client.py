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


class Client:

    @staticmethod
    def run():
        client_word = "client"
        with grpc.insecure_channel("localhost:9999") as channel:
            stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
            response = stub.getWord(spelling_bee_pb2.GetWord(get_word=client_word))
            print("Response: {} -- Score: {}".format(response.response, response.score))

    # Submits our word for approval
    # - returns true / false
    # - returns score
    def submit_word(self):
        with grpc.insecure_channel("localhost:9999") as channel:
            stub = spelling_bee_pb2_grpc.SpellingBeeServiceStub(channel)
            response, score = stub.getWord(spelling_bee_pb2.GetWord(get_word=self))
            return response, score




if __name__ == "__main__":
    Client.run()
