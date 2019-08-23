# sqlite3handler.py

Python class for communication with SQLite Database.

## Usage

```python
import datetime

import sqlite3handler

# SQLite DB file path
path = "db.sqlite"

qry_insert = f"INSERT INTO my_table (item, dt) VALUES ('New Item', '{datetime.datetime.now()}');"
qry_select = "SELECT * FROM my_table;"

# Classic way
db = sqlite3handler.Database(path)
db.execute(qry_insert)
print(db.query(qry_select))
db.close()

del db

# Using with statement
with sqlite3handler.Database(path) as db:
    db.execute(qry_insert)
    print(db.query(qry_select))
```