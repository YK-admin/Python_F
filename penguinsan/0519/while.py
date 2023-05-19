import sys
args = sys.argv
number =int(args[1])

total = 0
# while計算
while total<=100:
    total += number
    if total == 100:
        print("Just 100!",end="")
        break
    if total > 100:
        print("Over!", end="") 
        break  


