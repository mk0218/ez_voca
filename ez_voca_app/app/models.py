from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.schema import UniqueConstraint
from .database import Base
from .enumerations import EnglishWordClass, Topic


class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, autoincrement=True)

    spelling = Column(String, nullable=False)
    korean = Column(String, nullable=False)
    word_class = Column(Enum(EnglishWordClass, name="word_class"), nullable=False)

    __table__args__ = UniqueConstraint("spelling", "korean", name="_eng_kor_pair")

    en_description = Column(String)
    topic = Column(Enum(Topic, name="topic"))
    source = Column(String)
