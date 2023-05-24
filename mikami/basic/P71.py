# dateモジュール取得
from datetime import date

# 入力値取得
import sys
args = sys.argv

# YYYYMMDDを取得する
y = int(args[1][0:4])
m = int(args[1][4:6])
d = int(args[1][6:8])

# 休日かどうか判定する
if(date(y,m,d).strftime("%a") == "Sat" or date(y,m,d).strftime("%a") == "Sun"):
    is_holiday = True
else:
    is_holiday = False

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