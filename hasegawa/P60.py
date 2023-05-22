import sys
args = sys.argv

nums = args[1:]


# print(type(nums))

# 関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

     #あまりの値から奇数偶数判定
       
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")


for i in nums:
    rep_num = int(i)
    calcvalue(rep_num)    