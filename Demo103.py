import sqlite3

DB_PATH = 'data/demo103.sqlite'

if __name__ == '__main__':
    c1 = sqlite3.connect(DB_PATH)
    DROP_SQL = "DROP TABLE IF EXISTS EMPLOYEE";
    CREATE_SQL = '''
    CREATE TABLE EMPLOYEE
    (ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INTEGER NOT NULL,
    DEPT INT,
    ADDRESS CHAR(50));
    '''
    c1.execute(DROP_SQL)
    c1.execute(CREATE_SQL)
    c1.close()

