"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    def __init__(self, path):
        """Accepts a path to a file of words and turns it into a list of strings"""

        file = open(path)
        self.words = self.listify(file)
        print(f"{len(self.words)} words read")

    def listify(self, file):
        """Removes extra space/new line around each word in a file and creates a list"""

        return [word.strip() for word in file]

    def random(self):
        """Returns a random word"""

        return random.choice(self.words)