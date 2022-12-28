from typing import Optional
from enum import Enum


class EnglishWordClass(str, Enum):
    def __new__(cls, fullname: str, alias: Optional[str] = None):
        obj = str.__new__(cls, [fullname])
        obj._value_ = fullname
        obj.fullname = obj._value_
        if alias:
            obj.alias = alias
        else:
            obj.alias = fullname
        return obj

    @classmethod
    def includes(cls, str_: str):
        for ec in cls:
            if str_ == ec.fullname.lower() or str_ == ec.alias.lower():
                return True
        return False


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
