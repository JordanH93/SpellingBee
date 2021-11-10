import json
import os

""" Get relative paths to files"""
dirname = os.path.dirname(__file__)
DICTIONARY_PATH = os.path.join(dirname, "persistence/words_dictionary.json")
PANGRAMS_PATH = os.path.join(dirname, "persistence/pangrams.json")




class PangramDictionary:
    """
    1. Dictionary class that creates our pangrams.json lookup table
    2. Captures pangrams to public list variable 'pangrams' for later use
    3. Satisfies singleton pattern requirement
        - reasoning for singleton here is that we only need to create one instance of our dictionary class
        - that creates the pangrams.json file. Otherwise the file will be recreated with each instance
        - which is a waste of resources

    """

    __instance = None
    @staticmethod
    def get_instance():
        if PangramDictionary.__instance is None:
            PangramDictionary()
        return PangramDictionary.__instance

    def __init__(self):
        if PangramDictionary.__instance is not None:
            raise Exception("Unable to create another instance. This class is a singleton")
        else:
            PangramDictionary.__instance = self
            self.pangrams = {}

            with open(DICTIONARY_PATH) as json_file:
                words = json.load(json_file)
                for word in words:
                    if is_pangram(word):
                        self.pangrams[word] = ""

            with open(PANGRAMS_PATH, "w") as pangram_file:
                json.dump(self.pangrams, pangram_file)


def is_pangram(word_in):
    if len(set(word_in)) == 7 and 's' not in word_in:
        return True
    else:
        return False