import datetime
from P56database import session
from P56table import Items

#品目（品名と価格）を辞書型で定義
items = [
    {
        "name": "リンゴ",
        "price": 80,
        "category": "果物類"
    },
    {
        "name": "みかん",
        "price": 198,
        "category": "果物類"
    },
    {
        "name": "バナナ",
        "price": 150,
        "category": "果物類"
    },
    {
        "name": "ビール",
        "price": 360,
        "category": "酒類"
    },
    {
        "name": "日本酒",
        "price": 580,
        "category": "酒類"
    },
    {
        "name": "ラーメン",
        "price": 380,
        "category": "麺類"
    },
    {
        "name": "うどん",
        "price": 128,
        "category": "麺類"
    },
    {
        "name": "パスタ",
        "price": 258,
        "category": "麺類"
    },
]

for item in items:
    item = Items(
        name = item["name"],
        price = item["price"],
        category = item["category"],
    )

    session.add(item)
    session.commit()