import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import boto3
import json
from botocore.exceptions import ClientError


load_dotenv()


def get_secret():
    secret_name = "mySecretName"
    region_name = "myRegion"

    # Secrets Managerクライアントを作成
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    else:
        # シークレットを取得
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)


# 環境変数から値を取得
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
HOST_NAME = os.getenv('HOST_NAME', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'demo')
DB_PORT = os.getenv('DB_PORT', '3306')

# AWS環境の場合はsecrets managerから取得
IS_AWS_ENV = os.getenv('IS_AWS_ENV', 0)
if IS_AWS_ENV :
    secrets = get_secret()
    DB_USER = secrets['username'] or DB_USER
    DB_PASSWORD = secrets['password'] or DB_PASSWORD

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