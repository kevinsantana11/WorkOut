import pyodbc

connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-HRIJH4E;"
                      "Database=WorkOut_Db;"
                      "Trusted_Connection=yes;")

cursor = connection.cursor()
cursor.execute('SELECT * FROM Users')

for row in cursor:
    print('USERNAME = %s | PASSWORD = %s' % (row.username, row.password))




