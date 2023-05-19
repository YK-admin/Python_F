import sys
args = sys.argv

# 引数を変数に代入
input1 = args[1]
input2 = args[2]
input3 = args[3]

# たし算
sum = int(input1) + int(input2) + int(input3)

# 結果を表示
print(sum, end="")