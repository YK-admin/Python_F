item_dic = {"お茶":110, "コーヒー":100,
            "ソーダ":160, "コーンポタージュ":130}

for name in item_dic:
    price = item_dic[name]   

    item_list = "{0}：{1}円".format(name, price) 
    print (item_list)

input_amount = int(input("投入金額を入力してください"))

while 0 <= input_amount < min(item_dic.values()) or 10000 < input_amount:

    if input_amount > 10000:
        input_amount = int(input("10,000円を超える金額は投入できません。再度投入金額を入力してください"))

    elif input_amount < min(item_dic.values()):
        input_amount = int(input(input_amount+"円では購入できる商品がありません。再度投入金額を入力してください"))

    elif str(input_amount)[-1] != 0:
        input_amount = int(input("1円玉、5円玉は使用できません。再度投入金額を入力してください"))
    
    else:
        break


if input_amount >= min(item_dic.values()):
    input_item = ("何を購入しますか（商品名/cancel）")
    if input_item == "cancel":
        print(input_amount)
    # elif input_item in list(item_dic.keys()):
