from __future__ import annotations

import numpy as np
from jovin.sentence_parts.clause import Clause
from jovin.speech_parts import (Adjective, AdjectiveNoun, Adverb, Article,
                                BeingVerb, Conjunction, HelpingVerb, Name,
                                Noun, Preposition, Pronoun, ProperNoun, Verb)


class Phrase:
    def __init__(self, size=None) -> None:

        self.nouns = []
        self.adjectives = []
        self.adjective_nouns = []
        self.adverbs = []
        self.article = None

        if size is None:
            size = np.random.randint(0, 7)

        for _ in range(size):
            self.mutate()

    @property
    def chaos(self):
        return np.random.random()

    def mutate(self):
        #Perform a mutation, as in, evolution

        add_methods = [self.add_adjective, self.add_adjective_noun, self.add_adverb, self.add_noun]
        remove_methods = [self.remove_adjective, self.remove_adjective_noun, self.remove_adverb, self.remove_noun]

        chaos = self.chaos
        print("CHAOS", chaos)
        for _ in range(0, round(chaos*10)):
            if self.chaos > 0.3:
                #Do nothing
                continue

            if self.chaos > 0.2:
                #Add something
                np.random.choice(add_methods)()
            
            else:
                #remove something
                np.random.choice(remove_methods)()

        

    @staticmethod
    def convert_list_to_text(part_of_speech):
        return " ".join([str(x) for x in part_of_speech])

    @property
    def adverbs_text(self) -> str:
        return self.convert_list_to_text(self.adverbs)

    @property
    def adjectives_text(self) -> str:
        return self.convert_list_to_text(self.adjectives)

    @property
    def adjective_nouns_text(self) -> str:
        return self.convert_list_to_text(self.adjective_nouns)

    @property
    def nouns_text(self) -> str:
        return self.convert_list_to_text(self.nouns)

    @property
    def text(self) -> str:
        text: str = f"{self.adverbs_text} {self.adjectives_text} {self.nouns_text}"

        return text.strip()

    def __str__(self) -> str:
        return str(self.text)

    def add_adjective(self) -> Phrase:
        self.adjectives.append(Adjective())
        return self

    def add_noun(self, noun=None) -> str:
        if not noun:
            noun = Noun()
        self.nouns.append(noun)
        return self

    def add_article(self) -> Phrase:
        self.article = Article()
        return self

    def add_adjective_noun(self) -> Phrase:
        self.adjective_nouns.append(AdjectiveNoun())
        return self

    def add_adverb(self) -> Phrase:
        self.adverbs.append(Adverb())
        return self

    def remove_adjective(self) -> Phrase:
        number_of_adjectives = len(self.adjectives)
        if number_of_adjectives > 0:
            chaos = np.random.randint(number_of_adjectives)
            self.adjectives.pop(chaos)
        return self

    def remove_adjective_noun(self) -> Phrase:
        number_of_adjective_nouns = len(self.adjective_nouns)
        if number_of_adjective_nouns > 0:
            chaos = np.random.randint(number_of_adjective_nouns)
            self.adjective_nouns.pop(chaos)
        return self

    def remove_noun(self) -> Phrase:
        number_of_nouns = len(self.nouns)
        if number_of_nouns > 0:
            chaos = np.random.randint(number_of_nouns)
            self.nouns.pop(chaos)
        return self

    def remove_adverb(self) -> Phrase:
        number_of_adverbs = len(self.adverbs)
        if number_of_adverbs > 0:
            chaos = np.random.randint(number_of_adverbs)
            self.adverbs.pop(chaos)
        return self


