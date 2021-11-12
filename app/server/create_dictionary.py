"""
1. This class is used to create our pangrams dictionary
- We can use it to create pangrams of dynamic length

To do:
- Consider refactoring to make it not exclusively create pangrams but also a mixture of a set of chars that don't make
a pangram
"""


class CreateDictionary:
    def __init__(self, word_len, dictionary):
        self.pangrams = {}
        self.length = word_len

        for word in dictionary:
            if self.is_pangram(word):
                self.pangrams[word] = ""

    def is_pangram(self, word_in):
        if len(set(word_in)) == self.length and 's' not in word_in:
            return True
        else:
            return False
