import sys
args = sys.argv

# 給与を格納
salary = int(args[1])

if salary < 1000000:
    text = "支給額:{0}、税額:{1}".format(int(salary * 0.9), int(salary * 0.1))
    print(text, end="")
else:
    text = "支給額:{0}、税額:{1}".format(int((salary - 1000000) * 0.8 + 900000), int((salary - 1000000) * 0.2 + 100000))
    print(text, end="")