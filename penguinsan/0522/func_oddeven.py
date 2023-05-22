import sys

# 関数を定義
def calcvalue(num):
    # あまりを算出
    mod = num % 2

    # あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数",end="")
    else:
        print(str(num) + "は偶数",end="")

# 引数の取得
args = sys.argv[1:]  # プログラム名を除いた引数を取得

# 引数の数だけ繰り返し処理
for arg in args:
    number = int(arg)
    calcvalue(number)
