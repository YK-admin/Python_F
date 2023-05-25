from datetime import datetime
from database import session
from tables import Attendnum
import sys
args = sys.argv

# 引数代入
# 絶対こっちのほうがスマート
date = datetime.strptime(args[1], "%Y%m%d")
adult_people = int(args[2])
child_people = int(args[3])

attendlist = session.query(Attendnum.date, Attendnum.seq)\
.filter_by(date=date.date()).all()

seq = len(attendlist) + 1
attend = Attendnum(
    date = date.date(),
    seq = seq,
    adult = adult_people,
    child = child_people
)

session.add(attend)
session.commit()



