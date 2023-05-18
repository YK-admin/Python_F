import sys
args = sys.argv

# 入力の値をaに格納する
a = int(args[1])

# 偶数の処理
if a % 2 == 0:
    print("偶数", end="")
# 奇数の処理
else:
    print("奇数", end="")