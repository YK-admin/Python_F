import math

# 休日のリストを取得する
from datetime import date
from database import session
from tables import Mst_merhandise

mst_merhandise = session.query(Mst_merhandise).all()

print("-------------------")
print(mst_merhandise)

list = {}

# 飲み物リストを定義1
for value in mst_merhandise:
    if(value.number == 0):
        continue
    list[value.name] = {
        "id": value.id,
        "number": value.number,
        "price": value.price,
    }

def get_min_drink():
    min_drink = None

    # 初期テキスト
    for key in list.keys():
        print(list[key]["name"] + ":" + str(list[key]["number"]))
        if list[key]["price"] < min_drink or min_drink == None:
            min_drink = list[key]["price"]
    
    return min_drink

# お金リスト定義
coin = {
    5000: 0,
    2000: 0,
    1000: 0,
    500: 0,
    100: 0,
    50: 0,
    10: 0,
}

# 購入品リスト
purchase_drinks = {
    "お茶": 0,
    "コーヒー": 0,
    "ソーダ": 0,
    "コーンポタージュ": 0,
}

# 飲み物を定義
min_drink = get_min_drink()

# 入力を受ける最大のお金
max_money = 10000

# お金の入力を受け取る
while (True):
    money = int(input("購入金額を入力してください"))
    if( money > 10000 ):
        print("10,000円を超える金額は投入できません。再度購入金額を入力してください。")
    elif ( money % 10 != 0 ):
        print("1円と5円硬貨は使用できません。再度購入金額を入力してください。")
    elif ( money < min_drink ):
        print(str(money) + "円では買うことができません。再度購入金額を入力してください。")
    # 条件がすべて問題なければループを抜ける
    else:
        break

# 購入ロジック
while (True):
    select_drink = input("何を購入しますか？(商品名/cancel)")
    if not(select_drink in list.keys()):
        print("商品がありませんでした。")
        continue

    # 残額計算 リスト追加
    money = money - list[select_drink]
    purchase_drinks[select_drink] = purchase_drinks[select_drink] + 1

    select_drink_db = session.query(Mst_merhandise).filter_by(name=select_drink).first()
    select_drink_db.number = select_drink_db.number - 1
    if select_drink_db == 0:
        del list[select_drink]
        get_min_drink()
    session.add(select_drink_db)
    session.commit()

    # もう買えなければループ終了
    if ( money < min_drink ):
        break

    # 続けて購入しますか？
    while (True):
        message = input("続けて購入しますか？")
        if (message == "Y" or message == "N"):
            break
    
    # Nならループ終了
    if (message == "N"):
        break

# 終了したのでお釣り計算
print("お釣り")
for key in coin.keys():
    coin[key] = math.floor(money / key)
    money = money % key

    # ないなら出力飛ばし
    if (coin[key] == 0):
        continue

    # 出力する
    if (key <= 1000):
        print(str(key) + "円札：" + str(coin[key]) + "枚")
    else:
        print(str(key) + "円玉：" + str(coin[key]) + "枚")

print("---end---")