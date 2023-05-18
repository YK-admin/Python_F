import sys
args = sys.argv

# 引数を変数に代入
# 整数に変換
num = int(args[1])

# 奇数偶数判定
if num % 2 == 0:
    print("偶数", end="")
else: 
    print("奇数", end="")