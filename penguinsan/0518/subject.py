import sys
args= sys.argv

score_ma= int(args[1])
score_ja= int(args[2])
score_en= int(args[3])


# 点数の計算
total = score_ma + score_ja + score_en

# 合格基準に応じて結果を分析
result = "" #resultを空にする
if  (score_ma >=  70 and score_ja >=  70 and score_en >=  70) or total >= 220:
    if score_ma >= 50 and score_ja >= 50 and score_en >= 50:
        result ="合格"
    else:
        result = "不合格"
else:
    result ="不合格"

# 結果を表示
print(result, end="")


