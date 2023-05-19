# 引数で渡した数字の素因数分解を出力
import sys
args = sys.argv

# 引数を変数に代入
num = int(args[1])

# 素因数分解のリスト作成
prime_list = []

# 割り切れたら素因数分解のリストに追加

i = 2 
max = num
while i <= max:
    if num % i == 0:
        prime_list.append(i)
        num = num / i 
    else: i += 1

print(prime_list, end="")