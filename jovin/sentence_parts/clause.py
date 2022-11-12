import numpy as np
from jovin.sentence_parts.subject import Subject
from jovin.sentence_parts.predicate import Predicate

class Clause:
    def __init__(self) -> None:
        self.subject_phrase = Subject()
        self.predicate_phrase = Predicate()

    @property
    def text(self):
        return self.convert_list_to_text([self.subject_phrase, self.predicate_phrase])

    @staticmethod
    def convert_list_to_text(part_of_speech):
        return " ".join([str(x) for x in part_of_speech])

    def __str__(self) -> str:
        return self.text