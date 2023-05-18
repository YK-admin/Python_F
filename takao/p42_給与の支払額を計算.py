import sys
args = sys.argv

# 引数を変数に代入
salary = int(args[1])

# 条件分岐で給与と税率を計算
if salary <= 1000000:
    tax = salary * 0.1
else:
    tax = (salary - 1000000) * 0.2 + 1000000 * 0.1

pay_amount = salary - tax


print(f"支給額:{int(round(pay_amount))}、税額:{int(round(tax))}", end="")