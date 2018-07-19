import sqlite3

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT  * FROM localhistory"):
    print(row)

db.close()
