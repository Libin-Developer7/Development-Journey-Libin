from mysql import connector
class ExpenseTracker:
    def __init__(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="expense_tracker_task_db",
                use_pure=True

            )
            self.cursor=self.connection.cursor()
        except Exception as e:
            print(e)
# create table
    def create_table(self):
        query="""create table expenses(
                id int primary key auto_increment,
                name varchar(200) not null,
                email varchar(200) unique not null,
                expense_title varchar(200) not null,
                category enum("travel","food","fuel","bills"),
                amount_spent int not null,
                created_at datetime default current_timestamp   
        );"""
        self.cursor.execute(query)
        print("table created")
# expensetracker_instance=ExpenseTracker()
# expensetracker_instance.create_table()

# add data
    def add_data(self,**kwargs):
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")

            query=f"""insert into expenses ({columns}) values ({values});"""
            data=[v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
            print("data added")
        except Exception as e:
            print(e)
        
# expensetracker_instance=ExpenseTracker()
# expensetracker_instance.add_data(name="seb",email="seb@email.com",expense_title="travel to rome",category="travel",amount_spent=50000)
# expensetracker_instance.add_data(name="jeb",email="jeb@email.com",expense_title="travel to japan",category="travel",amount_spent=40000)

# retrieve all data
    def list_data(self):
        query="""select * from expenses"""
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for r in records:
            print(r)
# expensetracker_instance=ExpenseTracker()
# expensetracker_instance.list_data()

# delete a record
    def delete_data(self,id=None):
        query="""delete from expenses where id=%s"""
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("row deleted")
# expensetracker_instance=ExpenseTracker()
# expensetracker_instance.delete_data(id=5)

# update a record
    def update_data(self,id=None,**kwargs):
        placeholder=""
        for k,v in kwargs.items():
            placeholder+=k+"="+"%s"+","
        placeholder=placeholder.rstrip(",")
        query=f"""update expenses set {placeholder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
        print("row updated")
expensetracker_instance=ExpenseTracker()
expensetracker_instance.update_data(id=7,name="deb",email="deb@email.com")
expensetracker_instance.list_data()
