# 奇遇判定のプログラム

# 引数のライブラリをimport
import sys
args = sys.argv

# 変数numに引数を代入
num = args[1]

# 変数odd_numに文字列「奇数」を代入
odd_num = "奇数"

# 変数even_numに文字列「偶数」を代入
even_num = "偶数"

if int(num) % 2 == 0:
    print(even_num, end="")
else:
    print(odd_num, end="")