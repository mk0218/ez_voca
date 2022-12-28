from typing import Optional, Set
from pydantic import BaseModel
from .enumerations import Topic, EnglishWordClass as WdClass


class VocabularyBase(BaseModel):
    spelling: str
    korean: str
    word_class: WdClass


class VocabularyCreate(VocabularyBase):
    en_description: Optional[str] = None
    topic: Set[Topic]
    source: str


class Vocabulary(VocabularyBase):
    id: int
