import sys
from sqlalchemy import Column, String, Date, Integer
from P89_database import Base
from P89_database import ENGINE

# テーブル：Holidayの定義
class Holiday(Base):
    __tablename__ = 'holiday'
    holi_date = Column('holi_date', Date, primary_key= True )
    holi_text = Column('holi_text',String(20))

#水族館の来場者数テーブルの定義
class Holiday(Base):
    __tablename__ = 'attendnum'
    entry_date = Column('entry_date', Date, primary_key = True)
    seq = Column('seq', int, primary_key = True)
    adult = Column('adult', int)
    child = Column('child', int)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
