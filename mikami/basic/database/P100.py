# 休日のリストを取得する
from datetime import date
from database import session
from tables import Holiday

holiday_list = session.query(Holiday.holi_date).all()

# 入力値取得
import sys
args = sys.argv

# YYYYMMDDを取得する
y = int(args[1][0:4])
m = int(args[1][4:6])
d = int(args[1][6:8])

# 休日かどうか判定する(土日のみ)
if(date(y,m,d).strftime("%a") == "Sat" or date(y,m,d).strftime("%a") == "Sun"):
    is_holiday = True
else:
    is_holiday = False

# 休日かどうか判定する(祝日のみ)
for holiday in holiday_list:
    if holiday[0] == date(y,m,d):
        is_holiday = True

# 大人の人数・子供の人数を取得する
count_adult = int(args[2])
count_children = int(args[3])

# 価格を定義する
charge_adult_workday = 2000
charge_workday_children = 1200
charge_adult_holiday = 2400
charge_holiday_children = 1500

total_chage = 0

# 合計を計算する
if is_holiday:
    total_chage = total_chage + charge_adult_holiday * count_adult
    total_chage = total_chage + charge_holiday_children * count_children
else:
    total_chage = total_chage + charge_adult_workday * count_adult
    total_chage = total_chage + charge_workday_children * count_children

# 合計金額のみ取得
print(total_chage, end="")