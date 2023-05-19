import sys# 絶対つけるやつ

# 引数の取得
args = sys.argv # 絶対つけるやつ
sentence = args[1]
# 入力する数値
position = int(args[2])

# 英文を単語に分割
words = sentence.split()

# 指定した位置の単語を取得
# 指定された位置の単語をコンピューターの0,1,2に標準をあわせるために調整
word_at_position = words[position - 1]

# 結果を出力（改行なし）
print(word_at_position, end="")