from mysql import connector
class LibraryManagement:
    def __init__(self):
        try:
                self.connection = connector.connect(
                    host="localhost",
                    user="root",
                    password="Password@123",
                    database="library_management_db",
                    use_pure=True
                )
                self.cursor =self.connection.cursor()
                print("database connected")
        except Exception as e:
            print(e)
# lm_instance=LibraryManagement()

# creating table
    def create_table(self):
        query=""" create table books(
                id int primary key auto_increment,
                title varchar(200) not null,
                author varchar(200) not null,
                category enum ("mystery","fantasy","history","poetry"),
                added_date datetime default current_timestamp                  
        );"""
        self.cursor.execute(query)
        print("table created")
# lm_instance=LibraryManagement()
# lm_instance.create_table()

# adding data
    def add_data(self,**kwargs):
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")
            
            query=f"""insert into books ({columns}) values({values})"""
            data = [v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
            print("data added")
        except Exception as e:
                print(e)
# lm_instance=LibraryManagement()
# lm_instance.add_data(title="Pride and Prejudice",author="Jane Austin",category="poetry")
# lm_instance.add_data(title="1984",author="George Orwell",category="history")
# lm_instance.add_data(title="To Kill a Mockingbird",author="Harper Lee",category="mystery")

# fetching all data

    def list_books(self):
         query="select * from books"
         self.cursor.execute(query)
         records=self.cursor.fetchall()
         for r in records:
              print(r)
# lm_instance=LibraryManagement()
# lm_instance.list_books()

# deleting a row

    def delete_row(self,id=None):
         query="delete from books where id=%s"
         data=(id,)
         self.cursor.execute(query,data)
         self.connection.commit()

# lm_instance=LibraryManagement()
# lm_instance.delete_row(id=3)
# lm_instance.list_books()

# updating a row

    def update_row(self,id=None,**kwargs):
        placeholder=""
        for k,v in kwargs.items():
            placeholder+=k+"="+"%s"+","
        placeholder=placeholder.rstrip(",")
        query=f"""update books set {placeholder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
        self.connection.commit()
        print("row updated")

lm_instance=LibraryManagement()
lm_instance.update_row(id=1,title="Sense and Sensibility")
lm_instance.list_books()