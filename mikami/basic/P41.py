import sys
args = sys.argv

# 数学 国語 英語 の点数を格納
ma = int(args[1])
ja = int(args[2])
en = int(args[3])

# 合計算出
sum = ma + ja + en

# 1.合計点が220である
#   3教科とも70点以上
# 2.1科目も50点未満がない
if ((sum >= 220) or ((ma >= 70 and ja >= 70 and en >= 70 ))) and (ma >= 50 and ja >= 50 and en >= 50 ):
    print("合格", end="")
else:
    print("不合格", end="")