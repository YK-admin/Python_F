import sys
args = sys.argv

# 引数代入
num = int(args[1])

ans = ""
# 判定
if num%2==0:
    ans = "偶数"
else:
    ans = "奇数"

# 出力
print(ans, end="")