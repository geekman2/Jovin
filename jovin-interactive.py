#/bin/bash
from jovin.jovin import Sentence
from sandhammer import SandHammerWord


def main():
    sentence = str(Sentence())
    print('\n', sentence)
    keep = input("\nDoes this make sense? Type anything for yes, enter for no\n")

    interpret_as_no = ['no']
    if keep and keep.lower() not in interpret_as_no:
        #Write a completely random sentence alongside
        to_write = '\n'.join((sentence, str(Sentence())))
        with open(f'tmp/jovin/{SandHammerWord(filename="popular.txt")}.txt', 'a') as f:
            f.write(to_write)
            f.write('\n')



if __name__ == "__main__":
    #Run until exit
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Goodbye!")
            break