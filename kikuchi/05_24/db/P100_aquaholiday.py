from datetime import datetime
from database import session
from tables import Holiday
import sys
args = sys.argv

# 引数代入
# 絶対こっちのほうがスマート
date = datetime.strptime(args[1], "%Y%m%d")
big_people = int(args[2])
short_people = int(args[3])

# 料金表
price_table = {
    "nomal_day": [2000, 1200],
    "extra_day": [2400, 1500]
}

holidaylist = session.query(Holiday.holi_date)\
.filter_by(holi_date=date.date()).all()

# 合計料金算出
total = 0
if not(date.weekday() in [5, 6] or len(holidaylist) > 0):
    total += price_table["nomal_day"][0] * big_people
    total += price_table["nomal_day"][1] * short_people
else:
    total += price_table["extra_day"][0] * big_people
    total += price_table["extra_day"][1] * short_people

print(total, end="")
