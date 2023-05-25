from datetime import date
from P89_database import session
from P89_tables import Holiday

result = session.query(Holiday).filter_by(holi_date = date(2024,1,1)).delete()

# コミット

session.commit()