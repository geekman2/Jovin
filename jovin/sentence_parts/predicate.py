from jovin.phrases.verb_phrase import VerbPhrase

class Predicate:
    def __init__(self) -> None:

        self.verb_phrase = VerbPhrase()

        self.text = self.verb_phrase

    def __str__(self) -> str:
        return str(self.text)