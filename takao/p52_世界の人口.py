import sys
args = sys.argv

# 引数を変数に代入
num = int(args[1])

# ランキングを定義
ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(ranking[num-1], end="")