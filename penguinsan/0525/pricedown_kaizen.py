# 品目ごとに値引きを指定して実行する動作の実装

import sys # Pythonの組み込みモジュール

#引数を変数に代入
args = sys.argv # Pythonでコマンドライン引数を受け取る
item_classification = args[1] # 値下げする品目の分類（テキスト）
price_cut_amount = int(args[2]) # 値下げ額（数字）

#辞書型のデータ(品名:価格)を変数に代入
item = {
    "リンゴ":80 , "みかん":198, "バナナ":150, # 果物類
    "ビール":360, "日本酒":580, # 酒類
    "ラーメン":380, "うどん":128, "パスタ":258} # 麺類

#品目ごとの定義
fruits = ("リンゴ", "みかん", "バナナ") # 果物類
alcohol = ("ビール", "日本酒") # 酒類
noodles = ("ラーメン", "うどん", "パスタ") #麺類

# 果物類の値の更新
if item_classification == '果物類': # 入力テキストと変数の一致したとき
    for i in fruits: # 変数fruitで以下の動作を回す
        item[i] = item[i] - price_cut_amount # price_cut_amount分を減算する
        # 減算した値item[i]が1を下回った場合の条件分岐
        if item[i] < 1 :
            item[i] = 1 # 値を1に設定する

# 酒類の値の更新
# 果物類と同じ処理をする
if item_classification == '酒類': 
    for i in alcohol:
        item[i] = item[i] - price_cut_amount
        if item[i] < 1 :
            item[i] = 1

# 麺類の値の更新
# 果物類と同じ処理をする
if item_classification == '麺類':
    for i in noodles:
        item[i] = item[i] - price_cut_amount
        if item[i] < 1 :
            item[i] = 1

# 辞書型のデータをすべて出力する。item_classificationで指定した品目は減算した値が出力される。
print(item,end="") 