import sys　# 絶対つけるやつ

# リストの定義をタプルで並べる、タプルは昇順で要素を並べてくれる
population_ranking=("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 引数の取得
args = sys.argv # 絶対つけるやつ
rank = int(args[1])

# 指定された順位が有効な範囲内かどうかをチェックするための条件
if rank >= 1 and rank <= len(population_ranking):
    # 指定された順位に対応する要素を正しく取得する
    country = population_ranking[rank - 1]
    # 国名で表示する
    print(country,end="")