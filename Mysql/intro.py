"""
query for creating database
>create database database_name;
> eg:create database employee_db
query for listing all databases
>show databases;
query for switching to a database
>use database_name;
query for creating a table
> desc table_name;
show table details
>create table table_name(column_name1 data_type constraint, column_name2 data_type constraint)

Mysql datatypes:
number=>int,decimal,float
string=>varchar,char,text (char->only alphabets->char,sp char,numbers,char size is fixed, varies for varchar)
bool=>boolean
date=>DATETIME,DATE
enum=>all possible values

Mysql constraints:
null->value can be none
not null->mandatory
primary key->used for unique columns
foreign key->showing relation to another table
unique->no duplicates
default-> default value
check-> for checking conditions
auto increment-> automatically incrementing a value

sql query for inserting records

"""
