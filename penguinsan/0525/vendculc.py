import sys
from vend_change import change_in_all_money

# 引数の取得: 投入金額
args = sys.argv # 絶対つけるやつ
insert_price = int(args[1]) # 投入金額
product_price = int(args[2]) # 購入金額

# お釣り = 投入金額 - 購入金額
change = insert_price - product_price

print(change_in_all_money(change))

