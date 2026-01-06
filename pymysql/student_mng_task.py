from mysql import connector
class StudentManagement:
    def __init__(self):
        try:
                self.connection = connector.connect(
                    host="localhost",
                    user="root",
                    password="Password@123",
                    database="student_management_db",
                    use_pure=True
                )
                self.cursor =self.connection.cursor()
                print("database connected")
        except Exception as e:
            print(e)
    def create_table(self):
         query=""" create table students(
                    id int primary key auto_increment,
                    name varchar(200) not null,
                    email varchar(200) not null unique,
                    roll_number varchar(10) not null unique,
                    course enum ("DS","ML","AI"),
                    joined_date datetime default current_timestamp                  
         );"""
         self.cursor.execute(query)
         print("table created")
# sm_instance = StudentManagement()
# sm_instance.create_table()
    def add_data(self,**kwargs):
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")
            
            query=f"""insert into students ({columns}) values({values})"""
            data = [v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
            print("data added")
        except Exception as e:
             print(e)
# sm_instance = StudentManagement()
# sm_instance.add_data(name="dan",email="dan@email.com",roll_number=1122,course="DS")
# sm_instance.add_data(name="jen",email="jen@email.com",roll_number=1123,course="ML")
# sm_instance.add_data(name="matt",email="matt@email.com",roll_number=1124,course="ML")       

# fetch all data
    def list_students(self):
         query="select * from students"
         self.cursor.execute(query)
         records=self.cursor.fetchall()
         for r in records:
              print(r)
# sm_instance = StudentManagement()
# sm_instance.list_students()

# delete a row
    def delete_row(self,id=None):
         query="delete from students where id=%s"
         data=(id,)
         self.cursor.execute(query,data)
         self.connection.commit()
# sm_instance = StudentManagement()
# sm_instance.delete_row(id=3)
# sm_instance.list_students()

# update row
    def update_row(self,id=None,**kwargs):
        placeholder=""
        for k,v in kwargs.items():
            placeholder+=k+"="+"%s"+","
        placeholder=placeholder.rstrip(",")
        query=f"""update students set {placeholder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
        self.connection.commit()
        print("row updated")
sm_instance = StudentManagement()
sm_instance.update_row(id=4,name="patt")
sm_instance.list_students()

