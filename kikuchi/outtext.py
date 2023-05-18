import sys
args = sys.argv

# 引数を変数に代入
food = args[1]

#「I don’t like 入力した文字列」を出力
print("I don\'t like {0}".format(food), end="")