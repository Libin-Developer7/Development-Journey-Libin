# pip install mysql-connector-python
# pip list
# step 1 create a connector object
from mysql import connector
connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb",
    use_pure=True 
)
print("connection success")
# step 2 create a cursor object
cursor = connection.cursor()

# step 3 create query
query="""
create table user(
id int primary key auto_increment,
name varchar(200) not null,
email varchar(200) not null unique,
password varchar(200) not null
)

"""
cursor.execute(query)
print("table created")
cursor.close()
connection.close()