import sys
args= sys.argv

num= int(args[1])
if num % 2 == 0:
    print("偶数です")
else:
    print("奇数です")
