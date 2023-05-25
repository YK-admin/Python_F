import qrcode
import sys
import os

args = sys.argv

# ORコードを生成
img = qrcode.make(args[1])

# ファイルに保存
img.save(args[2])
