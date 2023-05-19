import sys
args = sys.argv

# 値を出力する
num = int(args[1])

# 人口数ランキングを定義
countries = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 値を出力する
print(countries[num - 1], end="")