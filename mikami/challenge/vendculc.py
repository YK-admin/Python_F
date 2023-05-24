

# 飲み物リストを定義1   
list = {
    "お茶": 110,
    "コーヒー": 100,
    "ソーダ": 160,
    "コーンポタージュ": 130,
}

# 初期テキスト 最安値の定義
for i in list.keys():
     print(i + str(list[i]))

# 細かい値を定義
# 配列の最小値を取得
min_drink = min(list.values())
# 入力を受ける最大のお金
max_manny = 10000

# お金の入力を受け取る
while (True):
    manny = int(input("購入金額を入力してください"))
    if( manny > 10000 ):
        print("10,000円を超える金額は投入できません")
    elif ( manny % 10 != 0 ):
        print("1円と5円硬貨は使用できません")
    elif ( min_drink < manny ):
        print("この金額では買うことができません")
    # 条件がすべて問題なければループを抜ける
    else:
        break

# 購入ロジック
while (True):
    select_drink = input("何を購入しますか？(商品名/cancel)")
    if()