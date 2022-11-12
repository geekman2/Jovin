import numpy as np

from jovin.speech_parts import ( Conjunction, Name,
                                Noun, Pronoun, ProperNoun, Article)
class Subject:

    words = [Noun, Pronoun, Name, ProperNoun]

    

    def __init__(self) -> None:

        if self.chaos > 0.5:
            compound = True
        else:
            compound = False

        if compound:
            conjunction = Conjunction()

            words = [
                self.generate_random_valid_word()
                for x in range(np.random.randint(1, 3))
            ]
            self.subject = f" {conjunction} ".join(str(x) for x in words)
        else:
            self.subject = self.generate_random_valid_word()

    def generate_random_valid_word(self):

        word = np.random.choice(self.words)()
        if self.chaos > 0.831:
            return f'{Article()} {word}'
        return word

    def __str__(self) -> str:
        return str(self.subject)

    @property
    def chaos(self):
        return np.random.random()