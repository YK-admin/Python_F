import sys
from sqlalchemy import Column, String, Date, Integer
from database import Base
from database import ENGINE

# 商品マスタ & 在庫
class Merchandise(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id', String(10), primary_key=True)
    name = Column('name', String(20))
    price = Column('price', Integer)
    stock = Column('stock', Integer)

# 商品在庫
# class Stock(Base):
#     __tablename__ = 'tbl_stock'
#     id = Column('id', String(10), primary_key=True)
#     stock = Column('stock', Integer)


# 貨幣格納
class Money(Base):
    __tablename__ = 'tbl_money'
    price = Column('price', Integer, primary_key=True)
    number = Column('number', Integer)

# メッセージ
class Message(Base):
    __tablename__ = 'tbl_message'
    seq = Column('id', Integer, primary_key=True, auto_increment = True)
    message = Column('message', String(100))
    datetime = Column('datetime', Date)



##################################################33

# テーブル
class Hinmoku(Base):
    __tablename__ = 'mst_hinmoku'
    id = Column('id', String(10), primary_key=True)
    name = Column('name', String(20))


# テーブル
class Zaiko(Base):
    __tablename__ = 'tbl_zaiko'
    id = Column('id', String(10), primary_key=True)
    unit = Column('unit', String(10), primary_key=True)
    unitprice = Column('unitprice', Integer, primary_key=True)
    stock  = Column('stock', Integer)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)