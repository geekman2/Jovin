"""
An RL Agent/Environment that uses 
Sandhammer to generate words
Jovin to generate sentences
Dingy to learn how to mutate
And Acid for it to float (learn) in
"""

from __future__ import annotations
from jovin.jovin import Sentence, Paragraph
from sandhammer import SandHammerWord


def main() -> list[str]:
    sentence = str(Sentence())
    print('\n', sentence)
    keep = input("\nDoes anything in this make sense? Type anything for yes, enter for no\n")

    interpret_as_no = ['no']
    if keep and keep.lower() not in interpret_as_no:
        #Write a completely random sentence alongside
        
        return True, sentence
    else:
        return False, sentence
        

def exit(to_write):
    if to_write:
        to_write = '\n'.join(to_write)
        sandhammer_word = SandHammerWord(filename="popular.txt")
        filename = f'tmp/jovin/{sandhammer_word}.txt'
        print(filename)
        with open(filename, 'a') as f:
            f.write(to_write)
            f.write('\n')
    print("Goodbye!")



def score_sentence(sentence:str, memory = {}):
    """
    Given a sentence, give a probability
    that we keep it. 
    """
    if not memory:
        return 1

    for tracked_sentence, reward in memory.items():

        if reward > 0:
            return 1
        else:
            return 0


if __name__ == "__main__":
    #Run until exit
    to_write = []
    memory = {}
    while True:
        try:
            keep, sentence = main()
            keep = float(bool(keep))
            print("You chose:", keep)
            score = score_sentence(sentence, memory)
            if keep and not score: #The machine tried to toss something good
                reward = -2
            elif keep == score:
                reward == 1
            else:
                reward = keep/score
            memory[sentence] = reward
            print("Reward:", abs(reward))


        
        except KeyboardInterrupt:
            exit(memory)
            break