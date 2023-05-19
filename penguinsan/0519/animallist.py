import sys

# 動物名前リストの定義
animal_list=["giraffe", "tiger", "zebra", "elephant", "lion"]

# 引数の取得
args = sys.argv
position = int(args[1])
animal_name = args[2]

# 要素の挿入
animal_list.insert(position, animal_name)

# 最後の要素の削除
animal_list.pop()

# リストの昇順ソート
animal_list.sort()

# 結果のリストを出力
print(animal_list,end="")