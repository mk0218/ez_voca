from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, database, models, schemas


app = FastAPI()


# Dependency
async def get_db():
    db = database.session()
    try:
        yield await db.begin()
    finally:
        await db.close()


@app.on_event("startup")
async def startup():
    await database.init_model()


@app.get("/vocabulary/{spelling}", response_model=List[schemas.Vocabulary])
async def read_vocabulary(spelling: str, db: AsyncSession = Depends(get_db)):
    return await crud.get_vocabulary_by_spelling(db, spelling=spelling)


@app.get("/vocabulary/{korean}", response_model=schemas.Vocabulary)
async def read_vocabulary_by_korean(korean: str, db: AsyncSession = Depends(get_db)):
    vocabulary = crud.get_vocabulary_by_korean(db, korean=korean)
    return await vocabulary


@app.post("/vocabulary/", response_model=schemas.Vocabulary)
async def create_vocabulary(
    voca: schemas.VocabularyCreate, db: AsyncSession = Depends(get_db)
):
    voca = crud.get_vocabulary(db, voca.spelling, voca.korean)
    if voca:
        raise HTTPException(status_code=400, detail="Already Exists")
    return await crud.create_vocabulary(voca)


@app.put("/vocabulary/{id}")
def update_vocabulary(id: int, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@app.delete("/vocabulary/{id}", response_model=schemas.Vocabulary)
def delete_vocabulary(id: int, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError
