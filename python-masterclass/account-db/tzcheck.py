import sqlite3
import pytz
import pickle

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT  * FROM history"):
    utc_time = row[0]
    # pickled_zone = row[3]
    # zone = pickle.loads(pickled_zone)
    zone = pytz.timezone('Australia/Adelaide')
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print(f'{utc_time}\t{local_time}\t{local_time.tzinfo}')

db.close()
