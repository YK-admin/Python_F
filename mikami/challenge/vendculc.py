import math

# 飲み物リストを定義1   
list = {
    "お茶": 110,
    "コーヒー": 100,
    "ソーダ": 160,
    "コーンポタージュ": 130,
}

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


# 初期テキスト 最安値の定義
for i in list.keys():
     print(i + str(list[i]))

# 細かい値を定義
# 配列の最小値を取得
min_drink = min(list.values())
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