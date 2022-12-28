import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

load_dotenv(verbose=True)

POSTGRES_USER = os.getenv("POSTGRES_USER", "ezvoca")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "ezvoca")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_DB = os.getenv("POSTGRES_DB", "ezvoca")

SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://"
    f"{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
)


engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def init_model():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
