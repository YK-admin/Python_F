# 自販機リスト
ven_list = {
    "お茶":110, "コーヒー":100, "ソーダ":160, "4コーンポタージュ":130
}
ven_list_num = {
    1:"お茶", 2:"コーヒー", 3:"ソーダ", 4:"コーンポタージュ"
}

# 投入金額について条件を満たすかどうか
flog = 0
while flog == 0:
    money = int(input("1.お茶：110\n2.コーヒー：100\n3.ソーダ：160\n4.コーンポタージュ：130\n投入金額を入力してください\n")
    )
    # 投入金額が100円以下
    if money < min(ven_list.values()):
        print(f"{money}円では購入出来る商品がありません。再度投入金額を入力してください")   
    # 投入金額が10000万以上   
    elif money >= 10000:
        print("10,000円を超える金額は投入出来ません。再度投入金額を入力してください")
    # 投入金額に1円玉、5円玉が含まれている
    elif money % 5 != 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
    else: flog = 1


# 商品購入について
y_or_n = "Y"
while money >= min(ven_list.values()) and y_or_n == "Y":
    item = input("何を購入しますか（番号/cancel）\n")
    item_num = ven_list[ven_list_num[int(item)]] 
    # cancelの場合おつりをだす
    if item == "cancel":
        break

    # 残金が100円より多い場合続けて購入するかどうか
    if money >= item_num + min(ven_list.values()):
        money = money - item_num
        y_or_n = input(f"残金：{money}円\n続けて購入しますか（Y/N）")

    # 選択した商品を買えない時
    elif money < item_num:
        y_or_n = input(f"そちらの商品は{money}円では購入出来ません\n続けて購入しますか（Y/N）")

    # 残金が100円より少ない時おつりをだす
    else: 
        break


# おつりを計算
oturi = money
m_50 = money // 5000 
money -= m_50 * 5000
m_10 = money // 1000
money -= m_10 * 1000
m_5 = money // 500
money -= m_5 * 500
m_1 = money // 100

# おつりを出力
print(f"おつり{oturi}円\n5000円札：{m_50}枚\n1000円札：{m_10}枚\n500円玉：{m_5}枚\n100円玉：{m_1}枚")

