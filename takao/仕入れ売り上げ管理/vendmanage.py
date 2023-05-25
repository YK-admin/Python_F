from cal_change import calchange
import pandas as pd

# 自販機リスト
ven_list = {
    "お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130
}
ven_list_num = {
    1:"お茶", 2:"コーヒー", 3:"ソーダ", 4:"コーンポタージュ"
}

# 投入金額について条件を満たすかどうか
flag = 0
while flag == 0:
    money = int(input("1.お茶：110\n2.コーヒー：100\n3.ソーダ：160\n4.コーンポタージュ：130\n投入金額を入力してください\n")
    )
    # 投入金額が100円以下
    if money < min(ven_list.values()):
        print(f"{money}円では購入出来る商品がありません。再度投入金額を入力してください")   
    # 投入金額が10000万以上   
    elif money > 10000:
        print("10,000円を超える金額は投入出来ません。再度投入金額を入力してください")
    # 投入金額に1円玉、5円玉が含まれている
    elif money % 5 != 0:
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
    else: flag = 1


# 商品購入について
y_or_n = "Y"
while money >= min(ven_list.values()) and y_or_n == "Y":
    item = input("1.お茶：110\n2.コーヒー：100\n3.ソーダ：160\n4.コーンポタージュ：130\n何を購入しますか（番号/cancel）\n")
    while item not in ["1","2","3","4","cancel"]:
        item = input("番号/cancelを入力してください\n")

    # cancelの場合おつりをだす
    if item == "cancel":
        print("キャンセルされました。おつりを出すよ") 
        break

    item_num = ven_list[ven_list_num[int(item)]]
    # 残金が100円より多い場合続けて購入するかどうか
    if money >= item_num + min(ven_list.values()):
        money = money - item_num
        y_or_n = input(f"残金：{money}円\n続けて購入する？（Y/N）")
        while y_or_n not in ["Y","N"]:
            y_or_n = input("Y/Nを入力してください")

    # 選択した商品を買えない時
    elif money < item_num:
        y_or_n = input(f"そちらの商品は{money}円では購入出来ません\n続けて購入する？（Y/N）")
        while y_or_n not in ["Y","N"]:
            y_or_n = input("Y/Nを入力してください")
            
    # 残金が100円より少ない時おつりをだす
    else:
        money = money - item_num
        print("他に買えるものがないのでおつりを出すよ") 
        break

# おつりを出力
calchange(money)