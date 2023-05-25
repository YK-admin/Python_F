import os
import sys
import json
from sqlalchemy import Column, String, DateTime, Integer, text
from database import Base
from database import ENGINE
from database import session
args = sys.argv
path = os.path.dirname(__file__)

# 商品マスタテーブル
class MasterMerchandise(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(20))
    price = Column("price", Integer)
    stock = Column("stock", Integer)

    def asdict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

# 貨幣格納テーブル
class TableMoney(Base):
    __tablename__ = 'tbl_money'
    price = Column("price", Integer, primary_key = True, autoincrement=False)
    number = Column("number", Integer)

    def asdict(self):
        return {
            "price": self.price,
            "number": self.number
        }

# メッセージテーブル
class TableMessage(Base):
    __tablename__ = 'tbl_message'
    seq = Column("seq", Integer, primary_key = True, autoincrement=True)
    message = Column("message", String(100))
    datetime = Column("datetime", DateTime, server_default=text('NOW()')) 

    def asdict(self):
        return {
            "seq": self.seq,
            "message": self.message,
            "datetime": self.datetime
        }

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)
    if len(session.query(MasterMerchandise).all()) == 0:
        with open(f"{path}/firstMasterMerchandise.json") as f:
            df = json.load(f)
            add_data = [
                MasterMerchandise(
                    id = i["id"],
                    name = i["name"],
                    price = i["price"],
                    stock = i["stock"]
                ) for i in df ]
            session.add_all(add_data)
            session.commit()

    if len(session.query(TableMoney).all()) == 0:
        with open(f"{path}/firstMoney.json") as f:
            df = json.load(f)
            add_data = [
                TableMoney(
                    price = i["price"],
                    number = i["number"],
                ) for i in df ]
            session.add_all(add_data)
            session.commit()
    

if __name__ == "__main__":
    main(sys.argv)