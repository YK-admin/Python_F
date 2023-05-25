import datetime
from database import session
from tables import Mst_merhandise

mst__list = [
    ["A000000001","お茶", 110, 1],
    ["A000000002","コーヒー", 100, 4],
    ["A000000003","ソーダ", 160, 0],
    ["A000000004","コーンポタージュ", 130, 3]
]

for mst in mst__list:
    mst = Mst_merhandise(
        id = mst[0],
        name = mst[1],
        price = mst[2],
        number = mst[3],
    )

    session.add(mst)
    session.commit()