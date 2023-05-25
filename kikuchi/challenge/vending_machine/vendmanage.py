from database import session
from vendtables import MasterMerchandise, TableMoney, TableMessage
from sqlalchemy import desc


items = session.query(MasterMerchandise).all()
moneylist = session.query(TableMoney).order_by(desc(TableMoney.price)).all()

min_price = -1
for obj in items:
    if obj.stock > 0:
        if min_price < 0 or min_price > obj.price:
            min_price = obj.price
        print(f"{obj.name}：{obj.price}円")

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

def separateCoin(price, moneylist):
    coins = {i.price:0 for i in moneylist}
    flag = True
    while flag:
        for m in moneylist:
            if price >= m.price and m.number >= 1:
                total -= m.price
                coins[m.price] += 1
                break
        if price == 0:
            flag = False
    return coins


total = input_coin()
coins = separateCoin(total, moneylist)
for i, v in enumerate(moneylist):
    moneylist[i].price += coins[v.price]
session.add_all(moneylist)
session.commit()


flag = True
while flag:
    if total < min_price:
        print(f"{total}円では購入できる商品がありません。再度投入金額を入力してください")
        total += input_coin()
        coins = separateCoin(total, moneylist)
        for i, v in enumerate(moneylist):
            moneylist[i].price += coins[v.price]
        session.add_all(moneylist)
        session.commit()
        continue
    
    print("何を購入しますか（商品名/cancel）")
    item_name = input()
    if item_name in [i.name for i in items]:
        for i in items:
            if i.name == item_name and i.stock >= 1:
                total -= i.price
                i.stock -= 1
                session.add(i)
                session.commit()
                break
                
        
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
oturi = separateCoin(total, moneylist)

for i, v in enumerate(moneylist):
    moneylist[i].price -= oturi[v.price]
    
session.add_all(moneylist)
print("おつり")
for i in oturi:
    if oturi[i] > 0:
        if i >= 1000:
            print(f"{i}円札：{oturi[i]}枚")

