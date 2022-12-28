from sqlalchemy.orm import Session
from . import schemas


async def create_vocabulary(db: Session, voca: schemas.VocabularyCreate):
    raise NotImplementedError


async def get_vocabulary_by_spelling(db: Session, spelling: str):
    raise NotImplementedError


async def get_vocabulary_by_korean(db: Session, korean: str):
    raise NotImplementedError


async def get_vocabulary(db: Session, spelling: str, korean: str):
    raise NotImplementedError
