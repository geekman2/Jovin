import numpy as np

from jovin.sentence_parts.clause import Clause
from jovin.speech_parts import Noun, Preposition, Pronoun, Name
from jovin.phrases.phrase import Phrase

class PrepositionalPhrase:

    valid_targets = [Phrase, Clause, Noun, Pronoun, Name]

    def __init__(self, object_of_the_prepostion=None) -> None:
        self.preposition = Preposition()
        if object_of_the_prepostion:
            self.object_of_the_preposition = object_of_the_prepostion
        else:
            self.object_of_the_preposition = self.randomly_select_target()()

    @property
    def text(self):
        if self.chaos > 0.9:
            return f'{self.preposition} {self.object_of_the_preposition} {PrepositionalPhrase()}'
        else:
            return f'{self.preposition} {self.object_of_the_preposition}'

    def __str__(self) -> str:
        return str(self.text)

    def randomly_select_target(self):
        return np.random.choice(self.valid_targets)

    @property
    def chaos(self):
        return np.random.random()