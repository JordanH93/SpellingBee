import uuid
"""
1. This class is used to create our user objects
- User has a name, email and password
- uuid / email will be our primary keys used for retrieving users in our db/json files

Note: Not used by any class yet
"""
class User:
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password # Password will be hashed
        self._id = uuid.uuid4()

    """Getters"""
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_id(self):
        return self._id

    """Setters"""
    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._name = email

    def set_password(self, password):
        self._password = password
