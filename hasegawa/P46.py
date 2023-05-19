# ある条件まで永遠足し算するプログラム

# 引数のライブラリをimport
import sys
args = sys.argv

num = int(args[1])

sum = 0

txt = "Over!"
while sum < 100:
    sum = sum + num 
    if sum == 100:
        txt = "Just "+str(sum)+"!"
print(txt, end="")
