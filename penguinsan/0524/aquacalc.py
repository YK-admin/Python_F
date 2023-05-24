# 水族館の入園料を計算しよう
from datetime import date
import sys

args= sys.argv
# day = int(args[1]) #20220521 がはいるけど、ymdに変換しなければいけない
y = int(args[1][0:4]) #0から4（4文字分）がはいる
m = int(args[1][4:6])
d = int(args[1][6:8])

adult_number = int(args[2]) #1がはいる
young_number = int(args[3]) #2がはいる

dt = date(d, m,d)

print(dt.strftime("%a"),end="")

#dt.strtimeがsatかsunかわかればよい

#土日
if datetime.weekdays()>4:
    adult_price = adult_number * 2400
    young_price = young_number * 1500
    pricesum_holiday = adult_price + young_price
    print(pricesum_holiday,end="")
else:
    adult_price = adult_number * 2000
    young_price = young_number * 1200
    pricesum_day = adult_price + young_price
    print(pricesum_day,end="")