import pymssql

# server = "CASC9MSDB04"
# user = getenv("PYMSSQL_TEST_USERNAME")
# password = getenv("PYMSSQL_TEST_PASSWORD")

conn = pymssql.connect(host=r'CASC9MSDD04',
    user=r'ports\seangi',
    password='EmptyN35t',
    database='Staging'
                       )

cursor = conn.cursor()

cursor.execute('SELECT * FROM DimCompany')
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()