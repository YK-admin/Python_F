from datetime import date
from database import session
from make_table import *

import pandas as pd

# 登録するデータの編集

shouhin_df = pd.DataFrame([["お茶", 110, 10],
                           ["コーヒー", 100, 20],
                           ["ソーダ", 160, 5],
                           ["コーンポタージュ", 130, 14],
                           ["ふるふるゼリー", 120, 4],
                           ["コーラ", 150, 10]],columns=["飲み物", "値段", "在庫"])

shouhin_df["num"] = list(range(1,len(shouhin_df)+1))


for n, p, s, i in shouhin_df.values.tolist():
    merchandise = Merchandise(
        id =  f"A{(i+1):09}",
        name = n,
        price = p,
        stock = s,
    )

    # INSERT処理
    session.add(merchandise)

    # コミット
    session.commit()

