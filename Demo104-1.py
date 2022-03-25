from Demo103 import DB_PATH
import sqlite3, time, os

print(os.getcwd())
c1 = sqlite3.connect(DB_PATH)

e1 = {'NAME': "Mark", "AGE": 45, 'DEPT': 1, 'ADDR': "Taipei"}
e2 = {'NAME': "John", "AGE": 25, 'DEPT': 2, 'ADDR': "Hsinchu"}
e3 = {'NAME': "Ken", "AGE": 35, 'DEPT': 3, 'ADDR': "Taipei"}
e4 = {'NAME': "Tim", "AGE": 55, 'DEPT': 4, 'ADDR': "Hsinchu"}
employees = [e1, e2, e3, e4]
SQL_DML = "INSERT INTO EMPLOYEE(NAME, AGE, DEPT,ADDRESS) VALUES(?,?,?,?)"
start = time.time()
for _ in range(5000):
    for e in employees:
        c1.execute(SQL_DML,(e['NAME'],e['AGE'],e['DEPT'], e['ADDR']))
        c1.commit()
    #c1.commit() # 21
#c1.commit() # 0.0439
c1.close()
end = time.time()
print("total spend:{}".format(end-start))