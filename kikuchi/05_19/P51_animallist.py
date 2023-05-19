import sys
args = sys.argv

# 引数代入
animal_index = int(args[1])
animal_name = args[2]

# 動物リスト
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 動物リストのanimal_indexにanimal_nameを代入
animals.insert(animal_index, animal_name)

# 最後の要素削除
animals.pop()

# 並び替え
animals.sort()

print(animals, end="")