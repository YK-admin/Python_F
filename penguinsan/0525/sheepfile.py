import sys

args = sys.argv
number =int(args[1])
i = 1 

with open('/home/matcha-23training/python_project/Python_F/penguinsan/0525/sheep.txt', mode='w', encoding="utf-8") as f:
    # ファイルを開く
    for i in range(1, number + 1):
        f.write("ひつじが" + str(i) + "匹\n")
        

# ファイルを閉じる
f.close()