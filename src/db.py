from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
ECHO_LOG = True

DATABASE = 'mysql:///python:python:mysql:python'

# DBとの接続
engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Sessionの作成
Session = sessionmaker(bind=engine)
session = Session()
