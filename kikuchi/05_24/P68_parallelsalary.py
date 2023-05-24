from func_salary import calcsalary
import sys
args = sys.argv

# 引数代入
salaries = args[1:]

# 各給与ごとに支給額と税額を計算・出力
for salary in salaries:
    result = calcsalary(salary)
    print(f"給与:{salary}、支給額:{result[0]}、税額:{result[1]}")