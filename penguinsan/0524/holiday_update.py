from datetime import date
from database import session # データベースへの接続
from tables import Holiday # テーブル定義

# 更新するデータの取得
holiday = session.query(Holiday).filter_by(holi_date=date(2024, 7, 1)).first()

# 更新するデータの更新
holiday.holi_text = "お盆"

# UPDATE処理
session.add(holiday)

# コミット
session.commit()