from datetime import date
from database import session # データベースへの接続
from tables import Holiday # テーブル定義

# 削除するデータを取得する
result= session.query(Holiday).filter_by(holi_date=date(2024, 7, 1)).delete()

# コミット
session.commit()