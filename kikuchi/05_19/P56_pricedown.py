import sys
args = sys.argv

# 価格表
all_items = {
    "果物類": ["リンゴ","みかん","バナナ"],
    "酒類":   ["ビール","日本酒"],
    "麺類":   ["ラーメン","うどん","パスタ"]
}
price_table = {
    "リンゴ":   80,
    "みかん":   198,
    "バナナ":   150,
    "ビール":   360,
    "日本酒":   580,
    "ラーメン": 380,
    "うどん":   128,
    "パスタ":   258
}


# 引数代入
category = args[1]
price = int(args[2])

# 値下げ
for i in all_items[category]:
    price_table[i] -= price
    if price_table[i] < 1:
        price_table[i] = 1

#出力
print(price_table, end="")

