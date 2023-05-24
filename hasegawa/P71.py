# 引数モジュールをimport

import sys
args = sys.argv

# 第2引数に日付（date）、第3引数に大人の人数(a_people)、第4引数に子供の人数(c_people)を代入

Y = int(args[1][0:4])
M = int(args[1][4:6])
D = int(args[1][6:8])

print(Y)
print(M)
print(D)


# a_people = args[2]

# c_people = args[3]



# 曜日を算出するためのdatetimeモジュールをimport


# from datetime import datetime

# date = datetime.date()
# print(date)

# # dt = date.weekday()



# 土日判定
