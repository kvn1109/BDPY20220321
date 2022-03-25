import sqlite3
import time
import os
from Demo103 import DB_PATH
c1 = sqlite3.connect(DB_PATH)
QUERY = "SELECT ID,AGE,ADDRESS FROM EMPLOYEE"
cursor1 = c1.cursor()
allRecords = cursor1.execute(QUERY).fetchmany(10)
print(len(allRecords))
print(type(allRecords))
for r in allRecords:
    print(r)
c1.close()