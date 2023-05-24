# 引数モジュールをimport

import sys
args = sys.argv

# 第2引数のYYYY部分を変数Yに代入、MM部分を変数Mに代入、DD部分を変数Dに代入

Y = int(args[1][0:4])
M = int(args[1][4:6])
D = int(args[1][6:8])

# 曜日の産出

# 曜日の産出の日付形式に変換
from datetime import date
dt = date(Y, M, D)

# 曜日を算出して数値形式でweekに代入
week = int(dt.strftime("%w"))

# 第3引数に大人の人数(a_people)、第4引数に子供の人数(c_people)を代入


a_people =int(args[2])

c_people = int(args[3])

# 平日の大人の金額をa_amount_weekdayの変数に代入
a_amount_weekday = 2000
# 休日の大人の金額をa_amount_holidayの変数に代入
a_amount_holiday = 2400
# 平日の子供の金額をa_amount_weekdayの変数に代入
c_amount_weekday = 1200
# 休日の子供の金額をa_amount_holidayの変数に代入
c_amount_holiday = 1500

# 土日判定
if 1 <= week <= 5:
    sum = a_people*int(a_amount_weekday)+c_people*int(c_amount_weekday)
else:
    sum = a_people*int(a_amount_holiday)+c_people*int(c_amount_holiday)
    
print(sum, end="")