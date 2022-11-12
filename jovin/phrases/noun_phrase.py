import numpy as np

from jovin.speech_parts import Noun, Pronoun, Name, ProperNoun, Adjective, Gerund
from jovin.phrases.phrase import Phrase

class NounPhrase:
    valid_targets = [Noun, Pronoun, Name, ProperNoun]

    def __init__(self) -> None:
        self.noun = self.randomly_select_target()
        self.adjectives = []
        self.gerunds = []
        self.phrase = Phrase()

        #Add gerund(s)
        for i in range(np.random.randint(0, 3)):
            self.gerunds.append(Gerund())



    def randomly_select_target(self):
        return np.random.choice(self.valid_targets)

    @property
    def chaos(self):
        return np.random.random()