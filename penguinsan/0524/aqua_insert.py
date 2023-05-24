from datetime import date
from database import session
from aqua_tables import Aquaattend

# 登録するデータの編集
aquaattend = Aquaattend(
    entry_date = date(2023, 5,24),
    seq = 1,
    adult =1,
    child =1,
)

# INSERT処理
session.add(aquaattend)

# コミット
session.commit()