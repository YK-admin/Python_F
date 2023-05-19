import sys
args = sys.argv

# 入力値定義・合計値初期化
num = int(args[1])
sum = 0

# is_just100のフラグ
flag = False

# 入力値から演算
while sum <= 100:
    if (sum == 100):
        flag = True
    sum = sum + num

# フラグによってメッセージ分岐
if flag: 
    print ("Just 100!", end="")
else:
    print ("Over!", end="")