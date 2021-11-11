import base64

from app.server import create_dictionary
from random import randint
import json
from app.objects import user
from app.server import connections

# test singleton
""" 
#test1 = dictionary.PangramDictionary() 
#test2 = dictionary.PangramDictionary()
"""

# Encoding example for passwords
"""
password = "Passw0rd1!".encode("utf-8")
encoded = base64.b64encode(password)
"""

# Write to users.json file example
"""
data = {'name': 'Jordan', 'email': 'jordan.hennessy@mycit.ie', 'password': '{}'.format(encoded)}
with open('app/server/persistence/users.json', 'w') as outfile:
    json.dump(data, outfile)
    outfile.close()
"""


# Append to a json file
"""
def write_json(new_data, filename='app/server/persistence/users.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["user_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


# python object to be appended
y = {"Name": "John",
     "email": "john@gmail.com",
     "password": "b'UGFzc3cwcmQxIQ=='"
     }

write_json(y)
"""

#Test connection
"""
y = {"Name": "John",
     "email": "john@gmail.com",
     "password": "b'UGFzc3cwcmQxIQ=='"
     }

c1 = connections.Connection
c1.append_users_json(y)
"""

#Retrieve json match
"""
filename='app/server/persistence/users.json'
with open(filename, 'r+') as file:
    file_data = json.load(file)
    for attrs in file_data['user_details']:
        if attrs['email'] == "jordan.hennessy@mycit.ie":
            print(attrs['name'])
        else:
            print("Found nothing.")
"""

#Test get user list and search
"""
c1 = connections.Connection
file_data = c1.get_users_json()

for attrs in file_data['user_details']:
        if attrs['email'] == "jordan.hennessy@mycit.ie":
            print(attrs['name'])
        else:
            print("Found nothing.")
"""

# test pangrams generation
"""
test1 = dictionary.PangramDictionary(9)
pangrams = test1.pangrams

# Pick a random pangram
rand_num = randint(0, len(pangrams))
random_pangram = list(pangrams.keys())[rand_num]
print(random_pangram)
print(set(random_pangram))
"""

# test user creation
"""
new1 = user.User("Jordan", "test@test.com", "pass")
new1.get_name()
"""

# test passing our json dictionary to create_dictionary
"""
c1 = connections.Connection.get_dictionary_json()
dictionary = create_dictionary.CreateDictionary(7, c1)
pangrams = dictionary.pangrams

# Pick a random pangram
rand_num = randint(0, len(pangrams))
random_pangram = list(pangrams.keys())[rand_num]
print(random_pangram)
print(set(random_pangram))
"""
