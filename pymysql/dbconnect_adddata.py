from mysql import connector
connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb",
    use_pure=True 
)
cursor=connection.cursor()

query="""
insert into user (name,email,password) values(%s,%s,%s)
"""
data=[
    ("vipin","vipin@gmail.com","vipin@123"),
    ("jibin","jibin@gmail.com","jibin@123"),
    ("lipin","lipin@gmail.com","lipin@123")
    ]
cursor.execute(query,data)
connection.commit() # auto commit is not available when doing with python
print("query executed...")
cursor.close()
connection.close()