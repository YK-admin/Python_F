# パッケージをインポート
import qrcode
import os


# QRコードを生成
img = qrcode.make("https://twitter.com/Sumida_Aquarium/status/1660903105796653057?s=20")

path = os.path.join(".", "files","image.png")
                    
# ファイルを保存
img.save(path)

