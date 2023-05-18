import sys
args = sys.argv

#引数を変数に代入
dis = int(args[1])

#初乗り運賃
price = 630

#1500円以上の場合の計算
if dis > 1500:
    add = (dis - 1500) // 344
    price = price + ((add + 1) * 98)

#出力
print(price, end="")