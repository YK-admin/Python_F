# 引数のライブラリをimport
import sys
args = sys.argv

add_animal_index = int(args[1])
add_animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animals.insert(add_animal_index, add_animal)

animals.pop()

animals.sort(key = None, reverse = False)

print(animals, end="")