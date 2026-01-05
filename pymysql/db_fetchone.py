from mysql import connector
connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb",
    use_pure=True
)
cursor=connection.cursor()
query="select * from user where id=%s"
data=(1,)
cursor.execute(query,data)
record=cursor.fetchone()
print(record)
cursor.close()
connection.close()
