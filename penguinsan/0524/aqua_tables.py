import sys
from sqlalchemy import Column, Date, Integer
from database import Base
from database import ENGINE

# テーブル: 'aquaattend'の定義
class Aquaattend(Base):
    __tablename__='aquaattend'
    entry_date = Column('entry_date', Date, primary_key= True) # 来場日：entry_date/data/key=True
    seq = Column('seq',Integer(), primary_key= True) # 連番：seq/int/key=True
    adult = Column('adult',Integer()) # 大人の人数：adult/int
    child = Column('child',Integer()) # 子供の人数：child/int

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__=="__main__":
    main(sys.argv)