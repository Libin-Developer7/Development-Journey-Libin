from mysql import connector
class Movies:
    def __init__(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="movies_task_db",
                use_pure=True,
            )
            self.cursor=self.connection.cursor()
            print("db connected")
        except Exception as e:
            print(e)

# create table movies
    def create_table(self):
        query=f"""create table movies(
                id int primary key auto_increment,
                title varchar(200) not null,
                language enum('malayalam','hindi','english','tamil','kannada') default 'english',
                genre enum('action','sci-fi','thriller','drama') default 'action',
                runtime int not null,
                rating decimal(3,1),
                check (rating between 1 and 10) 
        ); """

        self.cursor.execute(query)
        print("table created")
# movies_instance=Movies()
# movies_instance.create_table()

# add data to table
    try:
        def add_movies(self,**kwargs):
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")
            query=f"""insert into movies ({columns}) values({values});"""
            data=[v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
    except Exception as e:
        print(e)

# movies_instance=Movies()
# movies_instance.add_movies(title="inception",language="english",genre="sci-fi",runtime=120,rating=9.0)
# movies_instance.add_movies(title="interstellar",language="english",genre="sci-fi",runtime=180,rating=9.0)
# movies_instance.add_movies(title="dark knight",language="english",genre="action",runtime=190,rating=9.0)      
# print("data added") 

# fetch all data from table
    def list_movies(self):
        query="select * from movies"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for mov in records:
            print(mov)
# movies_instance=Movies()
# movies_instance.list_movies()

# retrieve one movie data
    def retrieve_movies(self,id=None):
        query="select * from movies where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        print(record)
# movies_instance=Movies()
# movies_instance.retrieve_movies(id=1)

# delete a record
    def delete_movies(self,id=None):
        query="delete from movies where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
# movies_instance=Movies()
# movies_instance.delete_movies(id=3)
# print("movie deleted")

# update a record
    def update_movies(self,id=None,**kwargs):
        for k,v in kwargs.items():
            place_holder=k+"="+"%s"+","
        place_holder=place_holder.rstrip(",")
        query=f"""update movies set {place_holder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
movies_instance=Movies()
movies_instance.update_movies(title="fight club",id=2)
movies_instance.list_movies()
print("data updated")
    
    