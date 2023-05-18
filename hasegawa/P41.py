#テスト結果判定プログラム

# sysモジュールをimport
import sys
args = sys.argv

# 第2引数にint型で変数math_scoreを代入
math_score = int(args[1])

# 第3引数にint型で変数jpn_scoreを代入
jpn_score = int(args[2])

# 第4引数にint型で変数eng_scoreを代入
eng_score = int(args[3])

sum_score = math_score + jpn_score + eng_score

if math_score >= 70 and jpn_score >= 70 and eng_score >= 70:
    print("合格", end="")
elif sum_score >= 220 and math_score >= 50 and jpn_score >= 50 and eng_score >= 50:
    print("合格", end="")
else:
    print("不合格", end="")