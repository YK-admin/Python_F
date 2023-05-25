import sys
args = sys.argv

#引数を変数に代入
#値下げ対象の種別
price_down_category = args[1]
#値下げ額
price_down_price = int(args[2])

#値引きするアイテムを取得
from P56database import session
from P56table import Items
price_down_items = session.query(Items).filter_by(category=price_down_category).all()

#値引き処理
for price_down_item in price_down_items:
    price_down_item.price = price_down_item.price - price_down_price
    if price_down_item.price < 0:
        price_down_item.price = 1
    session.add(price_down_item)
    session.commit()

#全アイテムを取得する
items = session.query(Items).all()

item_list = {}

for item in items:
    item_list[item.name] = item.price

print(item_list, end="")