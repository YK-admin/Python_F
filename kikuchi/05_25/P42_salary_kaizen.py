import sys
args = sys.argv

# 給与を代入
salary = int(args[1])

# 全体の給与の1割を税金として計算
tax = salary * 0.1

# 100万円を超える部分はさらに税金を１割追加
if salary>=1000000:
    tax += (salary-1000000) * 0.1

# 整数にする
tax = int(tax)

# 支給額を計算
payment = salary-tax

# 支給額と税額を表示
print(f"支給額:{payment:.0f}、税額:{tax:.0f}", end="")
