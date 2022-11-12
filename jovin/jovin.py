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
    def __init__(self, seed=None) -> None:

        if self.chaos > 0.5:
            compound = True
        else:
            compound = False

        if compound:
            conjunction = Conjunction()

            clauses = []
            for x in range(np.random.randint(1, 3)):
                phrase = self.generate_phrase()
                clauses.append(phrase)
            self.text = f" {conjunction} ".join(str(x) for x in clauses)
        else:
            self.text = self.generate_phrase()

    def generate_phrase(self):
        if self.chaos < 0.8:
            phrase = Clause()
        else:
            phrase = f'{Clause()} {PrepositionalPhrase()}'
        return phrase

    def __str__(self) -> str:
        return str(self.text)

    @property
    def chaos(self):
        return np.random.random()

class Paragraph:

    def __mul__(self, other):
        if isinstance(other, int):
            self.paragraph_list = [str(Paragraph()) for x in range(other)]
            return "\n".join(self.paragraph_list)

            return self

    def __init__(self) -> None:
        self.sentences = []
        number_of_sentences_in_paragraph = np.random.randint(1, 7)
        for i in range(number_of_sentences_in_paragraph):
            self.sentences.append(Sentence())

    def __str__(self):
        return '. '.join(str(x) for x in self.sentences)


    @property    
    def chaos(self):
        return np.random.random()

if __name__ == "__main__":
    # Generate the subject of a sentence
    subject = Subject()
    print("Just a subject:", subject)

    #Check that Gerunds function correctly
    gerund = Gerund()
    print("A verb that has been nouned:", gerund)

    # Generate a predicate
    predicate = Predicate()
    print("Just a predicate:", predicate)

    #Generate a bare phrase
    phrase = Phrase()
    print("A phrase that isn't a sentence at all:", phrase)

    #Generate a prepositional phrase
    prepositional_phrase = PrepositionalPhrase()
    print("Busy Prepositions", prepositional_phrase)

    # Generate a sentence manually
    print("Technically a sentence:", subject, predicate)

    # Generate a clause
    print("A clause, as in, a sentence:", Clause())

    # Create a new sentence
    print("A sentence:", Sentence())

    #Generate a paragraph
    print(Paragraph())

    #Write new output
    with open('tmp/jovin-output.txt', 'w') as f:
        f.write(Paragraph()*30)

    # Select the first sentence structure

    # Select the second sentence structure

    # Splice sentences by taking the subject from one and the predicate from another

    # Add a subject complement to a sentence that does not have one

    # Add a subject complement to a sentence that does already have one

    # Add a fragment to the beginning of the sentence

    # Add a prepositional phrase to the subject

    # Add a prepositional phrase to the predicate

    # Add a prepositional phrase to another prepositional phrase

    # Make the subject compound

    # Make the subject a pronoun

    # Add an adjective modifier to the subject

    # Add a compound adjective to the subject

    # Add an article to the subject

    # Convert a sentence structure into a sentence

    # Fill in the word
