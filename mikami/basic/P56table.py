import sys
from sqlalchemy import Column, String, Date, Integer
from P56database import Base
from P56database import ENGINE

class Items(Base):
    __tablename__ = 'items'
    id = Column("id", Integer, autoincrement=True, primary_key = True)
    name = Column("name", String(20))
    price = Column("price", Integer)
    category = Column("category", String(20))

def main(args):
    '''メイン関数'''
    Base.metadata.create_all(bind=ENGINE)
    print('')

if __name__ == "__main__":
    main(sys.argv)