# 入力を得てインチをセンチメートルに変換
# 変換のもとになる値
per_inch = 2.54
# ユーザーから入力を得る
# inch = input("How is inch?")
user = input("How is inch?")
inch = float(user)
# 計算する
cm = inch * per_inch
# 結果を表示
desc = "{0}inch = {1}cm" .format(inch, cm)
print(desc)