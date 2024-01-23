import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
load_dotenv()

# 環境変数から値を取得
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
HOST_NAME = os.getenv('HOST_NAME', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'demo')
DB_PORT = os.getenv('DB_PORT', '3306')

# 接続文字列を構築
ASYNC_DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{HOST_NAME}:{DB_PORT}/{DB_NAME}?charset=utf8"
# ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session