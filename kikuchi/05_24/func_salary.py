def calcsalary(salary):
    """給与から支給額、税額を計算します。"""
    # 引数を整数型に変換
    salary = int(salary)

    # 税額計算
    tax = salary * 0.1
    if salary>=1000000:
        tax += (salary-1000000) * 0.1
    tax = int(tax)

    # 支給額計算
    payment = salary-tax
    return [payment, tax]