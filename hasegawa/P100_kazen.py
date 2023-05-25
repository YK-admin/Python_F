# 引数モジュールをimport

import sys
args = sys.argv


# 第2引数のYYYY部分を変数Yに代入、MM部分を変数Mに代入、DD部分を変数Dに代入

Y = int(args[1][0:4])
M = int(args[1][4:6])
D = int(args[1][6:8])

# 祝日データベースのimport処理
from P89_database import session
from P89_tables import Holiday

# 祝日リストを全件取得
holidaylist = session.query(Holiday.holi_date).all()

# 曜日の産出の日付形式に変換
from datetime import date
dt = date(Y, M, D)

# 曜日を算出して数値形式でweekに代入
week = int(dt.strftime("%w"))

# 第二引数をinput_date、第3引数を大人の人数(a_people)、第4引数を子供の人数(c_people)に代入

# input_date = int(args[1])

adult_people =int(args[2])

child_people = int(args[3])

#売上表
sales_chart = {'W_adult':2000,'W_child':1200,'H_adult':2400,'H_child':1500}


# 合計値sumを定義
sum = 0


# 土日判定
if week in [1,2,3,4,5]:
    sum = adult_people*int(sales_chart['W_adult'])+child_people*int(sales_chart['W_child'])

    for holiday in holidaylist:
        if holiday[0] == dt:
            sum = adult_people*int(sales_chart['H_adult'])+child_people*int(sales_chart['H_child'])
else:
    sum = adult_people*int(sales_chart['H_adult'])+child_people*int(sales_chart['H_child'])
    
    
print(sum, end="")