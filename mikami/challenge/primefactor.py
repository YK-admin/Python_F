import sys
args = sys.argv

# 入力値を定義
num = 2023 #int(args[1])

# 因数のリスト定義
factor = []

# 素因数が2以上になるのでの初期値を定義する
i = 2

while not(num == 1):

    # 一回分の因数を探す
    if(num % i == 0):
        factor.append(i)
        num = num / i
    else:
        #iでなければ+1して次の数で試す
        i = i + 1

print(factor, end="")