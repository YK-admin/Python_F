import sys
args = sys.argv

# 引数代入
place1 = args[1]
place2 = args[2]

# 辞書型
stations = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35
}

try:
    # 計算
    between_length = stations[place1]-stations[place2]

    # マイナスなら変換
    between_length = abs(between_length)


    # 出力
    print("{:.2f}".format(between_length), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")