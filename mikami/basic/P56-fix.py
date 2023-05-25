import sys
args = sys.argv

#引数を変数に代入
#値下げ対象の種別
price_down_class = args[1]
#値下げ額
price_down_price = int(args[2])


#区分ごとの定義
fruits = ("果物類", "果物", "fruits")
alcohol = ("酒類", "アルコール", "alcohol")
noodle = ("麺類", "麵類", "noodle")


#品目（品名と価格）を辞書型で定義
items = [
    {
        "name": "リンゴ",
        "price": 80,
        "category": fruits
    },
    {
        "name": "みかん",
        "price": 198,
        "category": fruits
    },
    {
        "name": "バナナ",
        "price": 150,
        "category": fruits
    },
    {
        "name": "ビール",
        "price": 360,
        "category": alcohol
    },
    {
        "name": "日本酒",
        "price": 580,
        "category": alcohol
    },
    {
        "name": "ラーメン",
        "price": 380,
        "category": noodle
    },
    {
        "name": "うどん",
        "price": 128,
        "category": noodle
    },
    {
        "name": "パスタ",
        "price": 258,
        "category": noodle
    },
]

# 値引処理
for item in items:
    # 該当のクラス名の商品を値引きする
    if price_down_class in item["category"]:
        item["price"] = item["price"] - price_down_price
        # 値引きされた商品がマイナスなら1円に変換
        if item["price"] <= 0:
            item["price"] = 1

print(items, end="")