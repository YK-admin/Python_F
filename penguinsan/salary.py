# 給与の支払額の計算
import sys
args= sys.argv

income = int(args[1])

# 給与額 = income
# 支給額 = salary
# 全税額 = taxsum

if income < 1000000 :
    taxsum = int(income * 0.1)
else:
    taxsum = int((income - 1000000) * 0.2 + 1000000 * 0.1)

# 給与と税金の計算
salary = int(income - taxsum)

# 結果を表示
print("支給額:"+str(salary),end="")
print("、税額:"+str(taxsum),end="")

