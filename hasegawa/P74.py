# パッケージをインポート
import qrcode
# QRコードを生成

img = qrcode.make("https://www.mizuhobank.co.jp/retail/campaign/newlife_aes/index.html")

# モジュール「os」のimport
import os

# os.path.joinを利用して相対パスを生成
# 相対パス（"../files/*****.png"）となる

path = os.path.join("..","..","..","files", "echo_show.png")


# pngファイルの生成
img.save(path)