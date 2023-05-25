from datetime import date
from database import session
from tables import Holiday

# 登録するデータの編集
Holiday= Holiday(
    holi_date= date(2024, 1, 1),
    holi_text= "お正月"
)

# INSERT処理
session.add(Holiday)

# コミット
session.commit()