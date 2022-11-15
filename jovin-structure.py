"""
Jovin Structure takes as input an XML
and produces an object.

This object can be mutated and combined with
other objects of the same type
"""
import numpy as np
import os
from lxml import etree

class JovinSentenceStructure:
    def __init__(self, filename=None, filepath='var/sentences') -> None:

        self.filepath = filepath

        if filename is None:
            filename = self.randomly_select_structure()
            print(filename)
        self.filename = filename

        #Read xml into memory
        self.structure_xml = etree.parse(self.path_to_file)
        self.sentence_tree = self.structure_xml.getroot()
        assert len(self.sentence_tree) == 2, "A sentence has only two parts, subject and predicate"

        #Get subject and predicat trees
        self.subject_tree = self.sentence_tree[0]
        self.predicate_tree = self.sentence_tree[1]

        self.subject = JovinSubjectStructure(self.subject_tree)



    def randomly_select_structure(self):
        #Get a list of all filenames
        filenames = []
        for (dirpath, dirnames, filenames_x) in os.walk(self.filepath):
            filenames += filenames_x

        #Pick one
        return np.random.choice(filenames)

    @property
    def path_to_file(self):
        return os.path.join(self.filepath, self.filename)

class JovinSubjectStructure:
    def __init__(self, element) -> None:
        self.compound = element.find('compound')
        print(self.compound is not None)
        
        if self.compound is not None:
            for subject in self.compound.find('elements'):
                print(subject.text)
            print(self.compound.find('conjunction').text)

        else:
            

if __name__ == "__main__":


    structure1 = JovinSentenceStructure()
    structure2 = JovinSentenceStructure('turtles.xml')
    compund_subject = JovinSentenceStructure('argued.xml')