# import sys
# args = sys.argv

# # 引数を変数に代入
# depar = str(args[1])
# arriv = str(args[2])

# # 距離のデータを辞書型で定義
# dis_data = {
#     "東京":0.00, "品川":6.78, "新横浜":25.54,
#     "名古屋":342.02, "京都":476.31, "新大阪":515.35
# }

# # のぞみの停車駅の場合
# if (depar in dis_data.keys()) and (arriv in dis_data.keys()):
#     disctance = dis_data[arriv] - dis_data[depar]
#     print(round(abs(disctance),2), end="")

# # 例外処理
# else: 
#     print("のぞみの停車駅を引数に設定してください", end="")


import sys
args = sys.argv

# 引数を変数に代入
depar = str(args[1])
arriv = str(args[2])

# 距離のデータを辞書型で定義
dis_data = {
    "東京":0.00, "品川":6.78, "新横浜":25.54,
    "名古屋":342.02, "京都":476.31, "新大阪":515.35
}


try:
    disctance = dis_data[arriv] - dis_data[depar]
    print(round(abs(disctance),2), end="")
    
except:
    print("のぞみの停車駅を引数に設定してください", end="")