import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-ACJS2CB\SQLEXPRESS01;'
                      'Database=gimnasio;'
                      'Trusted_Connection=yes;'
                      'UID=cratospool;'
                      'PWD=123')

cursor = conn.cursor();
cursor.execute('select * from rol')

for row in cursor:
    print(row)


