import datetime
from database import session
from tables import Holiday

holiday = session.query(Holiday).filter_by(holi_date=datetime.date(2024,1,1)).first()

holiday.holi_text = "お正月"

session.add(holiday)

session.commit()