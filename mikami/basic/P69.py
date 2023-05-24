import sys
args = sys.argv

from P69_func import calcSalary

# 給与を格納
income = []
for i in range(1, len(args)):
    income.append(int(args[i]))

# 給与を3回計算する
for value in income:
    calcSalary(value)