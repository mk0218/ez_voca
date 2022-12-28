from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import UniqueConstraint

from .database import Base


class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, autoincrement=True)

    spelling = Column(String, nullable=False)
    korean = Column(String, nullable=False)
    word_class = Column(String, nullable=False)

    __table__args__ = UniqueConstraint("spelling", "korean", name="_eng_kor_pair")

    en_description = Column(String)
    topic = Column(String)
    source = Column(String)
