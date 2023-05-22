import sys# 絶対つけるやつ

# 引数の取得
args = sys.argv # 絶対つけるやつ
number1 = int(args[1])
number2 = int(args[2])

# 掛け算を行うだけの関数を定義
def mul(number1, number2):
    return number1 * number2

result = mul(number1, number2)
print("掛け算の結果:", result)