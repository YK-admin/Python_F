# 給与の支払額の計算
# 給与額 = income
# 支給額 = salary
# 全税額 = taxsum


def CalcSalary(income):

    if income < 1000000 :
        taxsum = int(income * 0.1)
    else:
        taxsum = int((income - 1000000) * 0.2 + 1000000 * 0.1)

    # 給与と税金の計算
    salary = int(income - taxsum)
    print("給与:" + str(income) + "、支給額:" + str(salary) + "、税額:" + str(taxsum))