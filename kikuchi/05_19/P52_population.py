import sys
args = sys.argv

# 引数代入
num = int(args[1])

# 引数が0ならエラー
if num <= 0:
    print("ValueError")
    exit()

# 国リスト
countries = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(countries[num-1], end="")

# import sys
# print(("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")[int(sys.argv[1])-1], end="")