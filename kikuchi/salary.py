import sys
args = sys.argv

# 給与を代入
salary = int(args[1])
tax = salary * 0.1
if salary>=1000000:
    tax += (salary-1000000) * 0.1
tax = int(tax)

payment = salary-tax
print(f"支給額:{payment}、税額:{tax}", end="")
