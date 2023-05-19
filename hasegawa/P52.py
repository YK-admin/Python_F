# 引数のライブラリをimport
import sys
args = sys.argv

# 変数rankに第二引数に1引いた数を代入
rank = int(args[1]) - 1

# 変数population_rankにタプルの値を代入
population_rank = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

# 変数rankに代入された値の順番で、タプルの値を表示
print(population_rank[rank], end="")