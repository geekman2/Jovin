"""
Mix together already written sentences in a mixer
"""
import numpy as np
from jovin.speech_parts import Name, Verb, ProperNoun, HelpingVerb, Pronoun, Noun
from sandhammer import SandHammerWord

class Character(SandHammerWord):
    """
    A character in a story
    """

    def __init__(self, wordlist=None, filename=None, filepath="var/wordlists/") -> None:
        super().__init__(wordlist, filename, filepath)

class PossessivePronoun(SandHammerWord):
    wordlist = ["his", "her", "its"]

    def __init__(self, wordlist=None, filename=None, filepath="var/wordlists/") -> None:
        super().__init__(wordlist=self.wordlist, filename=filename, filepath=filepath)

class BodyPart(SandHammerWord):
    wordlist = ["chest", "stomach", "heart"]

if __name__ == "__main__":

    character_list = [
        "Teresa Price",
        "Teresa Amy",
        "Dorothy Anne",
        "Watson Fisher",
        "Jones Harris"
    ]

    character1 = Character(wordlist=character_list)
    character2 = Character(wordlist=character_list)

    
    while str(character2) == str(character1):
        print(str(character1) == str(character2))
        character2 = Character(wordlist=character_list)

    sentences = [
        f'{character1} {Noun()}ed upon {PossessivePronoun()} feelings for {character2}',
        f'{PossessivePronoun()} {Noun()} would {Verb()} each {Noun()}. '
    ]

    print(np.random.choice(sentences))