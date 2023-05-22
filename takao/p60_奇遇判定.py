import sys
args = sys.argv

#関数を定義
def calcvalue(nums):

    for num in nums:
        #あまりを算出
        mod = int(num) % 2
        #あまりの値から奇数偶数判定
        if mod != 0:
            print(str(num) + "は奇数")
        else:
            print(str(num) + "は偶数")

# calcvalue(args[1:])
print(str(args[1:])[1:-1])
