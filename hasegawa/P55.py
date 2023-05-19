# 引数のライブラリをimport
import sys
args = sys.argv

# 第二引数を変数eng_sentenceに代入
eng_sentence = args[1]

# 第三引数を変数eng_word_orderに代入
# 入力数字とインデックスを合わせるために-1
eng_word_order = int(args[2])-1

# eng_sentenceを空白で分割して、変数wordsにリスト形式で代入
words = eng_sentence.split()

print(words[eng_word_order], end="")