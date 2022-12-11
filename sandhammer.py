import os
import random


class SandHammerWord:
    filename = None
    
    def __init__(self, wordlist=None, filename=None, filepath="var/wordlists/") -> None:
        if filename:
            self.filename = filename
            self.filepath = filepath
        if wordlist:
            self.wordlist = wordlist

        if self.filename:
            self.load_wordlist()
            

    def load_wordlist(self):
        # Load file from disk
        filepath = os.path.join(self.filepath, self.filename)
        with open(filepath) as f:
            wordlist = f.read()

        # Split into a list object
        self.wordlist = wordlist.split("\n")

    def __str__(self) -> str:
        return self.generate_word()

    def generate_word(self) -> str:
        word = None
        while not word:
            try:
                word = self.non_randomly_select_word()
            except IndexError:
                # print("The forces of chaos resist your efforts")
                pass
        return str(word)

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


if __name__ == "__main__":
    word = SandHammerWord(filename="10k-english.txt")
    noun = None
    adverb = SandHammerWord(filename="adverbs.txt")
    pronoun = SandHammerWord(filename="pronouns.txt")
    conjunction = SandHammerWord(filename="conjunctions.txt")
    verb = SandHammerWord(filename="verbs.txt")
    name = SandHammerWord(filename="names.txt")
    adjective = SandHammerWord(filename="adjectives.txt")

    for k in range(20):
        character1 = str(name)
        character2 = str(name)
        for i in range(random.randint(3, 8)):
            template1 = f"{name} had {word} but his {word} for {pronoun}"
            template2 = f"{adverb}, {adverb} {adjective} of a {word} and a {word} with two hundred {word} aboard, each of them {verb} for {word} and {word}.  Oh, {word}."
            template = random.choice([template1, template2])
            print(template)
