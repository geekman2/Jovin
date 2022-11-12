import random
from notalive import Sentence, Paragraph


class Thing:
    def __init__(self) -> None:
        pass


class Person:
    def __init__(self, *args, **kwargs) -> None:
        self.name = Name(**kwargs)
        self.punched = 0

    def __str__(self) -> str:
        return str(self.name)

    def punch(self, object):
        print(self.name, "punched", object)
        object.punched += 1

    def say(self, stuff):
        chaos = random.random()

        # Do not always print dialogue tags
        if chaos > 0.6:
            text = f'"{stuff}", {self.name} said'
        else:
            text = f'"{stuff}"'
        print(text)

    def get(self, object):
        print(self.name, "got", object)


class Name:
    def __init__(self, *args, **kwargs) -> None:
        assert "name" in kwargs, "name is required"
        self.name = kwargs["name"]

    def __str__(self) -> str:
        return self.name


class Tired(Thing):
    def __str__(self) -> str:
        return "tired"


def generate_dialogue(people, length=None):
    if length is None:
        length = random.randint(1, 15)

    for i in range(length):
        person = random.choice(people)
        person.say(Sentence(length=random.randint(2, 8)))


if __name__ == "__main__":
    bob = Person(name="Bob")
    tony = Person(name="Tony")
    narrator = Person(name="The Narrator")

    # bob.punch(tony)
    # tony.punch(bob)
    # bob.punch(tony)

    # bob.get(Tired())
    # bob.say(f'{tony} has been punched {tony.punched} times')
    people = [bob, tony]
    generate_dialogue(people)
    print(Paragraph() * random.randint(1, 4))
    generate_dialogue(people)
