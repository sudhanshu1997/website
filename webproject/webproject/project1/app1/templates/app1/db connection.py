import pymysql
#mydb=mysql.connector.connect(host="127.0.0.1",user="root",passwd="Root@123")


connection = pymysql.connect(
    host='localhost',
    port=3311,
    user='root',
    passwd='Root@123',
    db='medical'
)

print(connection)