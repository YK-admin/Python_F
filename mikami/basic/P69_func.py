#給与を計算する式
def calcSalary(salary):
    #100万未満は税金10%
    if salary < 1000000:
        text = "支給額:{0}、税額:{1}".format(int(salary * 0.9), int(salary * 0.1))
        print(text, end="")
    #100万以上は100万を超えた額を20% 100万未満は税金10%
    else:
        text = "支給額:{0}、税額:{1}".format(int((salary - 1000000) * 0.8 + 900000), int((salary - 1000000) * 0.2 + 100000))
        print(text)