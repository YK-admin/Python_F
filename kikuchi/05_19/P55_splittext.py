import sys
args = sys.argv

# 引数代入
text = args[1]
index = int(args[2]) - 1

# テキスト分割
split_text = text.split()

# 出力
print(split_text[index], end="")