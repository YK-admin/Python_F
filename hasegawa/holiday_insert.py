from datetime import date
# データべースへの接続
from P89_database import session
# テーブル定義
from P89_tables import Holiday

# 登録するデータの編集

holiday = Holiday(
    holi_date = date(2024, 1, 1),
    holi_text = "お正月"
)

# INSERT処理
session.add(holiday)

# コミット

session.commit()

