import sys
args = sys.argv

# 引数を変数に代入
# 整数に変換
num = int(args[1])

for i in range(1, num+1):
    print(f"ひつじが{i}匹")