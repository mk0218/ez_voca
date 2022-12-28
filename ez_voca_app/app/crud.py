"""CRUD utils"""
from sqlalchemy import column, String
from sqlalchemy.orm import Session


# from .database import database
from .enumerations import WordClass, PhraseClass
from .models import Vocabulary
from . import models, schemas


async def create_vocabulary(db: Session, voca: schemas.VocabularyCreate):
    # if WordClass.includes(voca.word_class) or PhraseClass.includes(voca.word_class):
    #     raise TypeError("Wrong English word class.")
    # else:
    #     voca.word_class =
    # isinstance(EnglishWordClass)

    created = models.Vocabulary(
        spelling=voca.spelling,
        word_class=voca.word_class,
        korean=voca.korean,
        en_description=voca.en_description,
        topic=voca.topic,
        source=voca.source,
    )
    await db.add(created)
    await db.commit()
    await db.refresh(created)
    return created


async def get_vocabulary_by_spelling(db: Session, spelling: str):
    return await db.Vocabulary.filter(Vocabulary.spelling == spelling).all()


async def get_vocabulary_by_korean(db: Session, korean: str):
    return await db.Vocabulary.filter(Vocabulary.korean == korean).all()


async def get_vocabulary(db: Session, spelling: str, korean: str):
    return await db.Vocabulary.filter(
        Vocabulary.spelling == spelling and Vocabulary.korean == korean
    ).first()


# 이렇게 하는 것이 맞는지 한 번 두고 보자.
