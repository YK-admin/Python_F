# 水族館の入園料を計算しよう
from datetime import date
import sys

args= sys.argv
# day = int(args[1]) #20220521 がはいるけど、ymdに変換しなければいけない
year = int(args[1][0:4]) #0から4（4文字分）がはいる
month = int(args[1][4:6])
day = int(args[1][6:8])

adult_number = int(args[2]) #1がはいる
young_number = int(args[3]) #2がはいる

# 日付オブジェクトを作成
dt = date(year, month, day)

# 曜日に応じて料金を計算
if dt.weekday()>4: # 土曜日(5)と日曜日(6)
    adult_price = adult_number * 2400
    young_price = young_number * 1500
    total_price = adult_price + young_price   
else:
    adult_price = adult_number * 2000
    young_price = young_number * 1200
    total_price = adult_price + young_price

print(total_price,end="")