import numpy as np
from jovin.sentence_parts.subject import Subject
from jovin.sentence_parts.predicate import Predicate
from jovin.sentence_parts.clause import Clause
from jovin.phrases.prepositional_phrase import PrepositionalPhrase
from jovin.speech_parts import Gerund
from jovin.phrases.phrase import Phrase
from jovin.jovin import Sentence
from jovin.jovin import Paragraph
from jovin.speech_parts import Name, Verb, ProperNoun, HelpingVerb, Pronoun


class Trait:
    def __init__(self) -> None:
        self.trait = self.generate_like()

    def __str__(self) -> str:
        return self.trait

    def generate_like(self):
        if True:
            likes = True
        
        thing_they_feel_about = f'{Verb()}ing {PrepositionalPhrase()}'

        if likes:
            return f'Likes: {thing_they_feel_about}'
        else:
            return f'Dislikes: {thing_they_feel_about}'

class Character():
    def __init__(self, num_traits=5) -> None:
        self.first_name = Name()
        self.last_name = Name()
        self.pronouns = Pronoun()
        self.name = f'{self.first_name} {self.last_name}'

        self.traits = [str(Trait()) for x in range(num_traits)]

    def __str__(self) -> str:
        return str(self.traits)

    def __repr__(self) -> str:
        return str(self)

class Event():
    def __init__(self, character_list) -> None:
        self.main_character = np.random.choice(character_list)
        self.secondary_character = np.random.choice(character_list)
        print("Secondary Character", self.secondary_character)
        self.event = f"{self.main_character} {HelpingVerb()} {Verb()} {PrepositionalPhrase(object_of_the_prepostion=self.secondary_character)}"
    def __str__(self) -> str:
        return str(self.event)
    def __repr__(self) -> str:
        return str(self)

if __name__ == "__main__":
    characters = {}

    number_of_characters = 10

    for i in range(number_of_characters):
        new_character = Character()
        characters[new_character.name] = new_character

    # for name, character in characters.items():
    #     print(name, character.traits)

    character_list = [character for character in characters]
    for i in range(3): #Make our first 3 characters our "Main" characters
        for k in range(i+3):
            character_list.append(character_list[i]) #Add a duplicate of the nth character

    print(f"Starting with {len(character_list)} characters")

    #character_list = ["Katie Banks", "Bobby 'Boobs' Ferrara", "Elijah Allen", "Antonio Simpson", "Kyle Ethan", "Thomas Ethan", "Teresa Joe", "Anne Kelly" ]
    #character_list = ["Data", "Geordi", "Picard", "Garak", "Julian", "Sisko", "Kirk", "Spock"]
    # for i in range(10):
    #     print(Event(character_list))
    #     print("Because", Event(character_list))
    #     print("and then")

    events = []
    for i in range(30):
        character = np.random.choice(character_list)
        secondary_character = np.random.choice(character_list)
        new_event = f'{character} {Verb()}ed {PrepositionalPhrase(object_of_the_prepostion=secondary_character)}'
        before_after = 'After'
        index_of_old_event = len(events)
        if not events:
            #print(new_event)
            pass
        else:
            before_after = np.random.choice(["Before", "After"])
            index_of_old_event = np.random.randint(len(events))
            old_event = events[index_of_old_event]
            #print(new_event)
            #print(f'{before_after} {old_event}, {new_event}')

        #keep = input("\nDooes this make sense? Type anything for yes, enter for no\n")
        keep = 'True'

        interpret_as_no = ['no']
        if keep and keep.lower() not in interpret_as_no:
            if before_after == 'After':
                events.insert(index_of_old_event+1, new_event)
            else:
                events.insert(index_of_old_event, new_event)

        #print('\n'*3)
        #print('==='*5)


    print('==='*5)
    print('\n'*3)
    print('==='*5)
    

    to_write = []
    for event in events:
        to_write.append(event)
        for i in range(3):
            to_write.append(str(Paragraph()))
        joining_phrases = ['and then', 'because', 'and as a result', 'nevertheless', 'meanwhile']
        joining_phrase = np.random.choice(joining_phrases)
        to_write.append(joining_phrase)

    with open('tmp/storyteller-output.txt', 'w') as f:
        f.write('\n'.join(to_write))

    print(character_list)
    print('\n'*3)
    print('==='*5)
