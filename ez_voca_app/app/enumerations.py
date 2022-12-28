from typing import Optional
from enum import Enum


class EnglishWordClass(Enum):
    def __init__(self, fullname: str, alias: Optional[str] = None):
        self.fullname = fullname
        if alias:
            self.alias = alias
        else:
            self.alias = fullname


class WordClass(EnglishWordClass):
    NOUN = ("noun", "n")
    VERB = ("verb", "v")
    ADJECTIVE = ("adjective", "adj")
    ADVERB = ("adverb", "adv")
    PREPOSITION = ("preposition",)
    PRONOUN = ("pronoun",)
    DETERMINER = ("determiner",)
    CONJUNCTION = ("conjunction",)
    INTERJECTION = ("interjection",)


class PhraseClass(EnglishWordClass):
    NOUN = ("noun phrase",)
    VERB = ("verb phrase",)
    ADJECTIVE = ("adjective phrase",)
    ADVERB = ("adverb phrase",)
    PREPOISITION = ("prepositional phrase",)


class Topic(Enum):
    pass
