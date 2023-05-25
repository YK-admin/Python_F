from datetime import date
from database import session
from aqua_tables import Aquaattend

# 登録するデータの編集
# 来場日、連番、大人の人数、子供の人数
aquaattend = Aquaattend(
    entry_date = date(2023, 5,24),
    adult =1,
    child =1,
)

# 連番を付与するためのクエリ
# 降順で並び変えておしりにある値を取ってきて、そこから+1をする処理
last_aquaattend = session.query(Aquaattend).order_by(Aquaattend.seq.desc()).first() # 最後に追加されたレコードが last_aquaattend という変数に格納される
if last_aquaattend: # もしlast_aquaend(最後の値)が存在する場合
    seq = last_aquaattend.seq + 1 # last_aquaendに+1する
else:
    seq = 1 #ない場合は1になる

# 連番を設定
aquaattend.seq = seq

# INSERT処理
session.add(aquaattend)

# コミット
session.commit()