import pandas as pd

import datetime as dt
from database import session
from make_table import *

q = session.query(Merchandise).filter(Merchandise.name == "お茶")
df = pd.read_sql(q.statement, session.bind)