import datetime as dt

import sys
args = sys.argv

week = dt.datetime.strptime(str(args[1]), '%Y%m%d').weekday()
adult_num = int(args[2])
child_num = int(args[3])


if week >= 5 : # 土曜日と日曜日の場合の処理
    total_fee = 2400*adult_num + 1500*child_num
else: 
    total_fee = 2000*adult_num + 1200*child_num

print(total_fee, end="")

