from sandhammer import SandHammerWord

# Define our parts of speech
class Article(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "articles.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class Noun(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "nouns.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class AdjectiveNoun(Noun):
    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist)


class Pronoun(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "pronouns.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class ProperNoun(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "proper-nouns.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class Name(ProperNoun):
    filename = "names.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist)


class Adverb(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "adverbs.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class Adjective(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "adjectives.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class Preposition(SandHammerWord):
    filepath = "var/wordlists/"
    filename = "prepositions.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class Verb(SandHammerWord):
    filepath = "var/wordlists"
    filename = "popular.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist, self.filename, self.filepath)


class HelpingVerb(Verb):
    filepath = 'var/wordlists/verbs'
    filename = "verbs-helping.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist)


class BeingVerb(Verb):
    filename = "verbs-being.txt"
    filepath = 'var/wordlists/verbs'

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist)


class Conjunction(SandHammerWord):
    filepath = "var/wordlists"
    filename = "conjunctions.txt"

    def __init__(self, wordlist=None) -> None:
        super().__init__(wordlist)

class Gerund:
    def __init__(self) -> None:
        self.verb = Verb()
        self.word = f'{self.verb}ing'
    def __str__(self) -> str:
        return str(self.word)
