import sys

args = sys.argv

# 文章を取得・文字列に変換
text = args[1]
num = int(args[2])
text_words = text.split()

# num番目の文字列を出力
print(text_words[num - 1], end="")