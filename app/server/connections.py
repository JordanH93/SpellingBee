import os
import json

"""
1. This class will create a single instance of connections to our json files and in the future a DB
- this is to ensure we don't have multiple instances manipulating data at the same time causing
- data inconsistencies
2. This class satisfies our singleton pattern requirement

To do:
- This class will later be refactored to separate our CRUD methods from our connections when/if we are using a DB
- set up db connection
"""

dirname = os.path.dirname(__file__)
USERS_PATH = os.path.join(dirname, "persistence/users.json")
DICTIONARY_PATH = os.path.join(dirname, "persistence/words_dictionary.json")


class Connection:
    __instance = None

    @staticmethod
    def get_instance():
        if Connection.__instance is None:
            Connection()
        return Connection.__instance

    def __init__(self):
        if Connection.__instance is not None:
            raise Exception("Unable to create another instance. This class is a singleton")
        else:
            Connection.__instance = self

    def append_users_json(self):
        with open(USERS_PATH, 'r+') as file:
            file_data = json.load(file)
            file_data["user_details"].append(self)
            file.seek(0)
            json.dump(file_data, file, indent=4)

    @staticmethod
    def get_users_json():
        with open(USERS_PATH, 'r+') as file:
            file_data = json.load(file)
            return file_data

    @staticmethod
    def get_dictionary_json():
        with open(DICTIONARY_PATH) as json_file:
            words = json.load(json_file)
            return words
