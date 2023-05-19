import sys
args = sys.argv

# 引数を変数に代入
# 整数に変換
num = int(args[1])

# 初期値を設定
add_sum = 0


while True:
    add_sum += num
    if add_sum == 100:
        print("Just 100!", end="")
        break   
    elif add_sum > 100:
        print("Over!", end="")
        break
