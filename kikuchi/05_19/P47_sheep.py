import sys
args = sys.argv

# 引数代入
num = int(args[1])

# ひつじを数える
for i in range(num):
    print(f"ひつじが{i+1}匹")