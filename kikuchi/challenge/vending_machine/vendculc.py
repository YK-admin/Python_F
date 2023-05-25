

items = {
    "お茶":     110,
    "コーヒー": 100,
    "ソーダ":   160,
    "コーンポタージュ":130
}
min_price = -1
for k in items:
    if min_price < 0 or min_price > items[k]:
        min_price = items[k]
    print(f"{k}：{items[k]}円")

def input_coin():
    flag = True
    input_num = 0
    while flag:
        try:
            input_num = int(input("投入金額を入力してください"))
            if input_num > 10000:
                print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
                continue
            if input_num % 10 != 0:
                print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
                continue
            return input_num
        except:
            print("error")

total = input_coin()
flag = True
while flag:
    if total < min_price:
        print(f"{total}円では購入できる商品がありません。再度投入金額を入力してください")
        total += input_coin()
        continue
    
    print("何を購入しますか（商品名/cancel）")
    item_name = input()
    if item_name in list(items.keys()):
        total -= items[item_name]
        
    elif item_name == "cancel":
        break

    else:
        print("そのような商品は存在しない")
        continue

    while True:
        print(f"残高：{total}円\n続けて購入しますか（Y/N）")
        answer = input()
        if answer in ["Y", "y", "N", "n"]:
            if answer in ["N", "n"]:
                flag = False
            break

# おつり計算
flag = True
coin_10 = 0
coin_50 = 0
coin_100 = 0
coin_500 = 0
coin_1000 = 0
coin_2000 = 0
coin_5000 = 0

while flag:
    if total >= 5000:
        total -= 5000
        coin_5000 += 1
    elif total >= 1000:
        total -= 2000
        coin_2000 += 1
    elif total >= 1000:
        total -= 1000
        coin_1000 += 1
    elif total >= 500:
        total -= 500
        coin_500 += 1
    elif total >= 100:
        total -= 100
        coin_100 += 1
    elif total >= 50:
        total -= 50
        coin_50 += 1
    elif total >= 10:
        total -= 10
        coin_10 += 1
    else:
        break

print("おつり")
if coin_5000 > 0:
    print(f"5000円札：{coin_5000}枚")
if coin_2000 > 0:
    print(f"2000円札：{coin_2000}枚")
if coin_1000 > 0:
    print(f"1000円札：{coin_1000}枚")
if coin_500 > 0:
    print(f"500円玉：{coin_500}枚")
if coin_100 > 0:
    print(f"100円玉：{coin_100}枚")
if coin_50 > 0:
    print(f"50円玉：{coin_50}枚")
if coin_10 > 0:
    print(f"10円玉：{coin_10}枚")











                



