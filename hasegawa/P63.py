# 引数のライブラリをimport
import sys
args = sys.argv

#第二引数を変数First_stationに代入
First_station = args[1]
#第三引数を変数Second_stationに代入
Second_station = args[2]

#辞書型のデータを変数stationに代入
stations = {
    "東京" : 0.00,
    "品川" : 6.78,
    "新横浜" : 25.54,
    "名古屋" : 342.02,
    "京都" : 476.31,
    "新大阪": 515.35,
}

#引き算の結果が負の整数になっても、正の整数として表示されるように駅間の差の絶対値を変数distanceに代入
try:
    distance = abs(stations[Second_station] - stations[First_station])
    print(round((distance),2), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
