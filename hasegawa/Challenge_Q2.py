item_dic = {"お茶":110, "コーヒー":100,
            "ソーダ":160, "コーンポタージュ":130}

for name in item_dic:
    price = item_dic[name]   

    item_list = "{0}：{1}円".format(name, price) 
    print (item_list)

input_amount = int(input("投入金額を入力してください"))

if input_amount >= min(item_dic.values()):
    input_item = ("何を購入しますか（商品名/cancel）")
    if input_item == "cancel":
        print(input_amount)

# if input_amount > 10000:
#     input_amout = int(input("10,000円を超える金額は投入できません。再度投入金額を入力してください"))

# elif input_amount < 100:
#     input_amout = int(input(input_amount+"円では購入できる商品がありません。再度投入金額を入力してください"))

#     if input_amount >= 100:
#             str(input("何を購入しますか（商品名/cancel）"))
