import numpy as np
from jovin.phrases.prepositional_phrase import PrepositionalPhrase
from jovin.speech_parts import Name, Verb, ProperNoun, HelpingVerb, Pronoun
from sandhammer import SandHammerWord

if __name__ == "__main__":
    plot_beats = [
        "Teresa put on pants",
        "Teresa took off her pants",
        "Teresa got fucked in her pussy",
        "Teresa got fucked in her ass",
        "Teresa ran away",
        "Dorothy Anne tried to intervene"
    ]

    character_list = [
        "Teresa Price",
        "Teresa Amy",
        "Dorothy Anne",
        "Watson Fisher",
        "Jones Harris"
    ]

    with open('var/beats.txt') as f:
        beats = f.read()
        plot_beats = beats.split('\n')

    for i in range(3):
        character = np.random.choice(character_list)
        secondary_character = np.random.choice(character_list)
        new_event = f'{character} {Verb()}ed {PrepositionalPhrase(object_of_the_prepostion=secondary_character)}'
        plot_beats.append(new_event)

    np.random.shuffle(plot_beats)

    joining_phrases = ['and then', 'because', 'and as a result', 'nevertheless', 'meanwhile']
    

    for beat in plot_beats:
        joining_phrase = np.random.choice(joining_phrases)
        print(beat)
        print(joining_phrase)