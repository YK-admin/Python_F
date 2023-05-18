# BMI判定プログラム
weight = float(input("体重は?"))
height = float(input("身長は？"))
# BMIの計算
height = height / 100 #mに直す
bmi = weight / (height * height)

# BMIの値に応じて結果を分析
result = "" #resultを空にする
if bmi > 18.5:
    result ="やせ型"
if (18.5 <= bmi) and (bmi < 30):
    result ="普通型"
if bmi >= 30:
    result ="肥満型"

# 結果を表示
print("BMI :", bmi)
print("判定：", result)