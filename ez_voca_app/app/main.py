from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from . import database, schemas


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


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/vocabulary/{spelling}", response_model=List[schemas.Vocabulary])
async def read_vocabulary(spelling: str, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@app.get("/vocabulary/{korean}", response_model=schemas.Vocabulary)
async def read_vocabulary_by_korean(korean: str, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@app.post("/vocabulary/", response_model=schemas.Vocabulary)
async def create_vocabulary(
    voca: schemas.VocabularyCreate, db: AsyncSession = Depends(get_db)
):
    raise NotImplementedError


@app.put("/vocabulary/{id}")
def update_vocabulary(id: int, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError


@app.delete("/vocabulary/{id}", response_model=schemas.Vocabulary)
def delete_vocabulary(id: int, db: AsyncSession = Depends(get_db)):
    raise NotImplementedError
