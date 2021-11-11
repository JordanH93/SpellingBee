from abc import ABCMeta, abstractstaticmethod


class ISpellingBee(meta=ABCMeta):
    @abstractstaticmethod
    def game_method():
        """Interface method"""


class Easy(ISpellingBee):
    def __init__(self):
        self.word_length = 5

    def game_method(self):
        """Easy mode game method code here"""


class Moderate(ISpellingBee):
    def __init__(self):
        self.word_length = 7

    def game_method(self):
        """Moderate mode game method code here"""


class Difficult(ISpellingBee):
    def __init__(self):
        self.word_length = 9

    def game_method(self):
        """Difficult mode game method code here"""


class SpellingBeeFactory:
    @staticmethod
    def build_game(game_type):
        if game_type == "Easy":
            return Easy()
        if game_type == "Moderate":
            return Moderate()
        if game_type == "Difficult":
            return Difficult()
        print("Invalid game type")
        return -1
