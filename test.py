from app.server import dictionary
from random import randint


test1 = dictionary.PangramDictionary()

""" test singleton """
#test2 = dictionary.PangramDictionary()

# test pangrams generation
pangrams = test1.pangrams

# Pick a random pangram
rand_num = randint(0, len(pangrams))
random_pangram = list(pangrams.keys())[rand_num]
print(random_pangram)
print(set(random_pangram))
