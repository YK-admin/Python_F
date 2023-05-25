# 引数のライブラリをimport
import sys
args = sys.argv

# 引数を変数countに代入
count = int(args[1])

# 変数add_numに0を代入
# add_num = 0

with open("../../../files/sheep.txt", mode="w", encoding="utf-8") as sheep_file:
    for i in range(1, count+1):
    # ファイルを開く（なければ作成する）
        # sheep_file = open("../../../files/sheep.txt", mode="w", encoding="utf-8") 

    # ファイルに書き込む
        # try:
        sheep_file.write("ひつじが"+str(i)+"匹\n")
    # finally:
sheep_file.close()  