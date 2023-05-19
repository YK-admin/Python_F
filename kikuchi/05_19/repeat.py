import sys
args = sys.argv

# 引数代入
num = int(args[1])

# 100までたし算
sum = 0
while 1:
    sum += num
    if sum==100:
        print("Just 100!", end="")
        break
    elif sum > 100:
        print("Over!", end="")
        break