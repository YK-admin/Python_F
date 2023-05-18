import sys
args = sys.argv

# 点数を代入
score_Math = int(args[1])
score_Jpn = int(args[2])
score_Eng = int(args[3])

# 判定し出力
if ((score_Math>= 70 and
    score_Jpn >= 70 and
    score_Eng >= 70) or score_Math+score_Jpn+score_Eng>=220) and (
        score_Math >= 50 and score_Jpn >= 50 and score_Eng >= 50):
    print("合格", end="")
else:
    print("不合格", end="")