import sys
args = sys.argv

# 引数代入
target = int(args[1])

# 2なら終了
if target == 2:
    print([2], end="")
    exit()

# 素因数分解
i = 2
imax = target
ans = []            # 答え入れる
while i < imax:
    if target % i == 0:
        target //= i
        ans.append(i)
    else:
        i += 1

# 答え表示
print(ans, end="")