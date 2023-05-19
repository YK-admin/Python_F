# 引数のライブラリをimport
import sys
args = sys.argv

# 引数を変数countに代入
count = int(args[1])

# 変数add_numに0を代入
add_num = 0

for i in range(1, count+1):
    add_num = add_num + 1
    print("ひつじが"+str(add_num)+"匹")