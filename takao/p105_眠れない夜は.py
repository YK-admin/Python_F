import sys
args = sys.argv

# 引数を変数に代入
# 整数に変換

# num = int(args[1])

num = 2

# sleep_file = open("./files/sleep.txt", mode="w", encoding="utf-8")

# for i in range(1, num+1):
#     sleep_file.write(f"ひつじが{i}匹\n")

# sleep_file.close()

sleep_file = open("./files/sleep.txt", encoding="utf-8")

# テキストを読み込む
read = sleep_file.read()

print(read)