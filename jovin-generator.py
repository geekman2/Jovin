from jovin.sentence_parts.subject import Subject
from jovin.sentence_parts.predicate import Predicate
from jovin.sentence_parts.clause import Clause
from jovin.phrases.prepositional_phrase import PrepositionalPhrase
from jovin.speech_parts import Gerund
from jovin.phrases.phrase import Phrase
from jovin.jovin import Sentence
from jovin.jovin import Paragraph
from jovin.speech_parts import Name, Verb, ProperNoun, HelpingVerb
    


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
    #print(Paragraph())

    #Write new output
    with open('tmp/jovin-output.txt', 'w') as f:
        to_write = Paragraph()*5
        #print(to_write)
        f.write(to_write)

    print("Wrote", len(to_write), "bytes")

    #Answer a "Why" question
    answer_to_why_question = f"Because {Name()} {Verb()}ed' {PrepositionalPhrase()} in {ProperNoun()}"
    while len(answer_to_why_question) > 60:
        answer_to_why_question = f"Because {Name()} {Verb()}ed {PrepositionalPhrase()} in {ProperNoun()}"
    print(answer_to_why_question)
    print(len(answer_to_why_question))

    #Answer "Who is Elijah"
    answer_to_why_question = f"A {Phrase()} {PrepositionalPhrase()}"
    while len(answer_to_why_question) > 60:
        answer_to_why_question = f"A {Phrase()} {PrepositionalPhrase()}"
    print(answer_to_why_question)
    print(len(answer_to_why_question))

    #Answer "What is the candle map incident"
    answer_to_why_question = f"That time {Name()} {HelpingVerb()} {Verb()} {PrepositionalPhrase()}"
    while len(answer_to_why_question) > 60:
        answer_to_why_question = f"That time {Name()} {HelpingVerb()} {Verb()} {PrepositionalPhrase()}"
    print(answer_to_why_question)
    print(len(answer_to_why_question))

    #Answer "When did the incident happen"

    #Where did "The Candle Map Incident" happen?

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
