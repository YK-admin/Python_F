from datetime import date
from database import session
from create_aquaatend import Attendnum

import sys
args = sys.argv

# YYYYMMDDを取得する
y = int(args[1][0:4])
m = int(args[1][4:6])
d = int(args[1][6:8])

# 大人の人数・子供の人数を取得する
count_adult = int(args[2])
count_children = int(args[3])

attend = Attendnum(
    entry_date = date(y, m, d),
    adult = count_adult,
    child = count_children
)

session.add(attend)
session.commit()