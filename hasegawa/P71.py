# 引数モジュールをimport

import sys
args = sys.argv

# 第2引数のYYYY部分を変数Yに代入、MM部分を変数Mに代入、DD部分を変数Dに代入

Year = int(args[1][0:4])
Month = int(args[1][4:6])
Day = int(args[1][6:8])

# 曜日の産出の日付形式に変換
from datetime import date
dt = date(Year, Month, Day)

# 曜日を算出して数値形式でweekに代入
week = int(dt.strftime("%w"))

# 第3引数に大人の人数(a_people)、第4引数に子供の人数(c_people)を代入


adult_people =int(args[2])

child_people = int(args[3])


#売上表
sales_chart = {'W_adult':2000,'W_child':1200, 'H_adult':2400, 'H_child':1500}

# 合計額の変数を定義
sum = 0

# 土日判定
if 1 <= week <= 5:
    sum = adult_people*int(sales_chart['W_adult'])+child_people*int(sales_chart['W_child'])
else:
    sum = adult_people*int(sales_chart['H_adult'])+child_people*int(sales_chart['H_child'])
    
print(sum, end="")