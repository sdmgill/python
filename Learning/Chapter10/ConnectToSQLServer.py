import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=CASC9MSDB03;"
                      "Database=stg_JDICMPortsAmerica_Prd;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT name FROM sys.tables')

for row in cursor:
    statement = "DROP TABLE " + str(row).strip("(),''")
    statement = statement[:-3]
    print(statement)