import os
import sys
args = sys.argv

args = sys.argv
path = os.path.dirname(__file__)
# 引数代入
num = int(args[1])
text = ""
# ひつじを数える
for i in range(num):
    text+=f"ひつじが{i+1}匹\n"

with open(f"{path}/sheep.txt", mode="w", encoding="utf-8") as tf:
    tf.write(text)
