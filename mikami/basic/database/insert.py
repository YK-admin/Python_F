import datetime
from database import session
from tables import Holiday

holiday__list = [
    # ["20230101","元日"],
    ["20230109","成人の日"],
    ["20230211","建国記念の日"],
    ["20230223","天皇誕生日"],
    ["20230321","春分の日"],
    ["20230429","昭和の日"],
    ["20230503","憲法記念日"],
    ["20230504","みどりの日"],
    ["20230505","こどもの日"],
    ["20230717","海の日"],
    ["20230811","山の日"],
    ["20230918","敬老の日"],
    ["20230923","秋分の日"],
    ["20231009","スポーツの日"],
    ["20231103","文化の日"],
    ["20231123","勤労感謝の日"],
]

for holiday in holiday__list:
    holiday = Holiday(
        holi_date = datetime.datetime.strptime(holiday[0], '%Y%m%d').date(),
        # holi_date = date(int(holiday[1][0:4]), int(holiday[1][4:6]), int(holiday[1][6:8]))
        holi_text = holiday[1]
    )

    session.add(holiday)
    session.commit()