import numpy as np

from jovin.speech_parts import Verb, HelpingVerb, BeingVerb

class VerbPhrase:

    # Insert Verb multiple times to give it a higher chance of being selected
    words = [Verb, Verb, Verb, Verb, HelpingVerb, BeingVerb]

    def __init__(self) -> None:
        self.chaos = np.random.random()

        # Initialize text with a verb
        self.text = np.random.choice(self.words)()

        # convert the word to past tense, for narrative reasons
        #self.text = f"{self.text}d"

        # Sometimes, add a helping verb
        threshold_for_adding_a_helping_verb = 0.8
        if self.chaos > threshold_for_adding_a_helping_verb:
            # Add an article before word
            self.text = f"{HelpingVerb()} {self.text}"

    def __str__(self) -> str:
        return str(self.text)