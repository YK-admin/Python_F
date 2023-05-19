import sys
args = sys.argv

# 入力値変換
list_animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]
num = int(args[1])
animal = args[2]

#リストにアニマルを挿入
list_animal.insert(num, animal)

del list_animal[-1]

list_animal = sorted(list_animal)

print(list_animal, end="")