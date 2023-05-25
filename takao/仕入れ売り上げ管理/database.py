from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

# mysqlのDBの設定

user = os.getenv("DB_USER","root")
password = os.getenv("DB_PASSWORD","mysql")
host = os.getenv("DB_HOST","localhost")
database = os.getenv("DB_DATABASE","ENSHU")

DATABASE = f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8"

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo = True # 実行の度にSQLが出力
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# table.pyで継承する
Base = declarative_base()
Base.query = session.query_property()