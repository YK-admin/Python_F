# 給与計算の関数を作成

def calcsalary(*salary):
    """
    給与計算を行う計算
    Args:
        salary(int) : 給与の額面

    Returns:
        pay_amount(int) : 支給額
        tax(int) : 税額

    Examples:
        >>> calcsalary(10000000)
        80100000, 19900000
    """

    for sal in salary:

        if sal <= 1000000:
            tax = sal * 0.1
        else:
            tax = (sal - 1000000) * 0.2 + 1000000 * 0.1

        pay_amount = sal - tax

        print(f"支給額:{int(round(pay_amount)):,}、税額:{int(round(tax)):,}")

