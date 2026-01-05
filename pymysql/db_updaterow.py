from mysql import connector
connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb",
    use_pure=True
)
cursor=connection.cursor()
query="update user set name=%s where id=%s"
data=("subin",2)
cursor.execute(query,data)
connection.commit()
print("row updated")
cursor.close()
connection.close()