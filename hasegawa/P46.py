# ある条件まで永遠足し算するプログラム

# 引数のライブラリをimport
import sys
args = sys.argv

# 引数を変数numに代入
num = int(args[1])

# 変数sumに0を代入
sum = 0

# 変数txtに"Over!"を代入
txt = "Over!"

# 変数sumが100未満のときのみ足し算を繰り返し処理する
while sum < 100:
    sum = sum + num 
    # sumが100になったときのみ変数txtに"Just 100!"を代入
    if sum == 100:
        txt = "Just "+str(sum)+"!"
print(txt, end="")