from datetime import date
from tables import Holiday
from database import session

holiday = Holiday(
    holi_date = date(2024, 1, 1),
    holi_text = "お正月"
)

session.add(holiday)
session.commit()