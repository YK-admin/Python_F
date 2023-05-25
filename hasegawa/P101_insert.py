# 引数モジュールをimport
import sys
args = sys.argv

# 第2引数のYYYY部分を変数Yに代入、MM部分を変数Mに代入、DD部分を変数Dに代入

Y = int(args[1][0:4])
M = int(args[1][4:6])
D = int(args[1][6:8])

# 第3引数を大人の人数(adult_people)、第4引数を子供の人数(child_people)に代入

adult_people =int(args[2])

child_people = int(args[3])

# 曜日の産出の日付形式に変換
from datetime import date
dt = date(Y, M, D)

from datetime import date
from P89_database import session #データベースの接続
from P101_tables import attendnum #テーブル定義

#登録するデータの編集

Attendnum = attendnum(
    entry_date = dt,
    seq = 1 + session.query(attendnum.entry_date).filter_by(entry_date = dt).count(),
    adult = adult_people,
    child = child_people
)

# Insert処理
session.add(Attendnum)

# コミット
session.commit()