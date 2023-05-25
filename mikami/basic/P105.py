import sys
args = sys.argv

# 入力値定義
num = int(args[1])

import os
path = os.path.join("../../..",  "files",  "test.txt")

n = 1

with open(path, mode="r", encoding="utf-8") as a_file:
    for line in a_file:
        if "<" in line:
            n = n + 1

b_file = open(path, mode="a", encoding="utf-8")

b_file.write("<" + str(n) + "回目の実行>\n")

for i in range(1, num + 1):
    b_file.write("ひつじが" + str(i) + "匹\n")

b_file.write("\n")