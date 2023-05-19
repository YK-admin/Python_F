import sys # 絶対つけるやつ
# 引数の取得
args = sys.argv # 絶対つけるやつ
place_from = args[1]
place_to = args[2]
# 辞書型でデータを並べてく
distance= {'東京':0.00,'品川':6.78,'新横浜':25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}


try:
    # 拠点間の距離を求める
    distance_between = abs(distance[place_to] - distance[place_from])
    # 距離を小数第2位まで出力
    print(f"{distance_between:.2f}",end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")
