# 10000, 5000, 1000, 500, 100, 50, 10円の大きい順で割っていく（for 変数 in money）。
def change_in_all_money(change):
    # リスト
    money_list = [10000, 5000, 1000, 500, 100, 50, 10]
    for m in money_list:
        num_of_bills = change // m  # お札または硬貨の枚数
        change = change % m  # 残りのお釣り
        print('{}円札または硬貨：{}枚'.format(m, num_of_bills))

