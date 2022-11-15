from __future__ import annotations

import numpy as np
from jovin.speech_parts import Gerund
from jovin.sentence_parts.clause import Clause
from jovin.sentence_parts.predicate import Predicate
from jovin.sentence_parts.subject import Subject
from jovin.phrases.phrase import Phrase
from jovin.phrases.prepositional_phrase import PrepositionalPhrase

from jovin.speech_parts import Conjunction

class Sentence:

    def __init__(self, size=None) -> None:
        self.compound = self.is_compound
        self.phrases = [] #Phrases are ordered


        if self.is_compound:
            conjunction = Conjunction()

            for x in range(np.random.randint(1, 3)):
                phrase = self.generate_phrase()
                self.phrases.append(phrase)
            self.sentence =  f" {conjunction} ".join(str(x) for x in self.phrases)
        else:
            self.sentence =  self.generate_phrase()
        
    @property
    def is_compound(self):
        if self.chaos > 0.5:
            compound = True
        else:
            compound = False

        return compound

    @property
    def text(self):
        while not self.sentence:
            if self.is_compound:
                self.sentence =  f" {Conjunction()} ".join(str(x) for x in self.phrases)

            if not self.sentence:
                self.sentence = str(Sentence())
        return self.sentence

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.text)


    def mutate(self, index=None):
        if index is None:
            #If no index is specified, choose a random index
            index = np.random.randint(0, len(self.phrases))

        phrase = Phrase(self.phrases[index])
        phrase = phrase.mutate()
        self.phrases[index] = str(phrase)

        return self

    def expand(self, index = None):
        if index is None:
            #If no index is specified, choose a random index
            index = np.random.randint(0, len(self.phrases))

        phrase = Phrase(self.phrases[index])
        phrase = phrase.expand()
        self.phrases[index] = str(phrase)
        return self

    def contract(self, index = None):
        if index is None:
            #If no index is specified, choose a random index
            index = np.random.randint(0, len(self.phrases))

        phrase = Phrase(self.phrases[index])
        phrase = phrase.contract()
        self.phrases[index] = str(phrase)
        return self
    

        

    def generate_phrase(self):
        if self.chaos < 0.2:
            phrase = str(Clause())
        else:
            phrase = f'{Clause()} {PrepositionalPhrase()}'

        if self.chaos > 0.6:
            new_phrase = Phrase()
            if new_phrase:
                phrase = f'{new_phrase}, {phrase}'

        return phrase

    

    @property
    def chaos(self):
        return np.random.random()

class Paragraph:

    def __mul__(self, other):
        if isinstance(other, int):
            self.paragraph_list = [str(Paragraph()) for x in range(other)]
            return "\n".join(self.paragraph_list)

            return self

    def __init__(self, low=10, high=30) -> None:
        self.sentences = []
        number_of_sentences_in_paragraph = np.random.randint(low, high)
        for i in range(number_of_sentences_in_paragraph):
            self.sentences.append(Sentence())

    def __str__(self):
        return '. '.join(str(x) for x in self.sentences )


    @property    
    def chaos(self):
        return np.random.random()

