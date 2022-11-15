#/bin/bash
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
        to_write = [sentence, str(Sentence())]
        return to_write
    else:
        return []
        

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

if __name__ == "__main__":
    #Run until exit
    to_write = []
    while True:
        try:
             to_write += main()

        
        except KeyboardInterrupt:
            exit(to_write)
            break
            