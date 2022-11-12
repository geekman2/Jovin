"""
This file is not alive

But it is written to be difficult to debug and interpret

As it grows, it will seem to take on a life of its own
"""

import random
import numpy as np

# Load file from disk
with open("var/google-10000-english.txt") as f:
    tenkay = f.read()

# Convert from string to list
takey = tenkay.split()
print(len(takey))

# Print a random word by index
randint = random.randint(0, len(takey))


class Word:
    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.word

    def __init__(self, wordlist, index=None) -> None:
        self.wordlist = wordlist
        if index is None:
            self.word = self.non_randomly_select_word()
        else:
            self.word = self.wordlist[index]
            self.index = index

    def non_randomly_select_word(self):

        # The percent values in the comments are subject to change
        chaos = random.random()
        # print("CHAOS",chaos)
        top_hundredth = int(len(self.wordlist) / 100)
        bottom_25 = int(len(self.wordlist) / 4)
        top_75 = int(len(self.wordlist) - bottom_25)

        # There is a N% chance we choose from the middle 50th percentile
        if chaos > 0.25 and chaos < 0.75:
            bag_of_words = self.wordlist[bottom_25:top_75]

        elif chaos > 0.75 and chaos < 0.85:
            bag_of_words = self.wordlist[:top_75]

        # There is a N% chance we choose from the top 10th percentile
        elif chaos > 0.1:
            bag_of_words = self.wordlist[:top_hundredth]

        # There is a N% chance we choose from the bottom 25th percentile
        elif chaos < 0.1:
            bag_of_words = self.wordlist[:bottom_25]

        else:
            bag_of_words = self.wordlist

        return random.choice(bag_of_words)

    @property
    def part_of_speech(self):
        if random.random() > random.random():
            return "noun"
        if random.random() > random.random():
            return "adjective"
        if random.random() > random.random():
            return "verb"
        else:
            return "fail"


class Sentence:
    wordlist = takey

    def __mul__(self, other):
        if isinstance(other, int):
            self.sentence_list = [str(Sentence()) for x in range(other)]
            self.sentence = ". ".join(self.sentence_list)

            return self

    def __str__(self) -> str:
        return self.sentence

    def __init__(self, template=None, length=None) -> None:

        if length == None:
            length = random.randint(1, 20)

        if template:
            # Check if it's a Jinja template
            # Disabled so I don't have to import Jinja
            # This is a possible feature, not a definite
            # part of the interface
            assert True

        self.sentence_list = []
        for i in range(length):
            word = str(Word(wordlist=self.wordlist))
            self.sentence_list.append(word)

        self.sentence = " ".join(self.sentence_list)


class Block(Sentence):

    low = 1
    high = 10

    def __init__(self, size: int = None) -> None:
        if size is None:
            size = random.randint(self.low, self.high)
        self.size = size

        self.sentence_list = []
        for i in range(size):
            word = str(Sentence())
            # Prevent duplicate words in the same sentence
            while word in self.sentence_list:
                word = str(Sentence)
            self.sentence_list.append(word)

        self.sentence = ". ".join(self.sentence_list)

    def __mul__(self, other):
        if isinstance(other, int):
            self.sentence_list = [str(Block()) for x in range(other)]
            self.sentence = "\n".join(self.sentence_list)
            return self

    @property
    def text(self):
        return Sentence() * self.size


class Paragraph(Block, Sentence):
    low = 3
    high = 5


if __name__ == "__main__":
    output = Paragraph() * 30
    print(output)
    with open("tmp/output.txt", "w") as f:
        f.write(str(output))
