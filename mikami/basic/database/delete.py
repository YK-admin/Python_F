import datetime
from database import session
from tables import Holiday

result = session.query(Holiday).filter_by(holi_date=datetime.date(2024,1,1)).delete()

session.commit()