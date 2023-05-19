# 引数のライブラリをimport
import sys
args = sys.argv

# 変数add_animal_indexに第二引数を代入
add_animal_index = int(args[1])

# 変数add_animalに第三引数を代入
add_animal = args[2]

# 変数animalにリストの値（文字列）を代入
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 特定のindex番号に値を追加する関数insertを指定
animals.insert(add_animal_index, add_animal)

# リストの最後のインデックス番号の値を削除する関数popを指定
animals.pop()

# リストを昇順にソートする関数sortを指定
animals.sort(key = None, reverse = False)

print(animals, end="")

print(args)