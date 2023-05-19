import sys
args = sys.argv

# 引数を変数に代入
num = int(args[1])
animal = str(args[2])

# 動物のリストを作成
animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 特定の位置に動物名を挿入
animal_list.insert(num, animal)

# リストの最後の動物名を消す
# del animal_list[-1]
animal_list.pop()

# 昇順
animal_list.sort()

# 出力
print(animal_list, end="")