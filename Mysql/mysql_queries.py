"""> insert into table_name(title,location,description) values('drainage issue','mg road','drainage issue on mg road')

sql query for fetching all records from a table
> select * from table_name; -> returns all values from table
> select title,status from issues;
> select * from issues where id=1;      where used when condition exists
> select * from issues where id<4;
updating a column - update used to edit data already inserted
> update issues set status=0 where id=2;
deleting a row, only entire row can be deleted
> delete from issues where id=3;
alter used to edit table, while update used to update column
alter table table_name add column_name constraints;
alter table table_name modify column_name constraints;

aggregate functions
max(),min(),count(),sum(),average()

joins
innerjoin - matching records in both tables
select * from left_table innerjoin right_table on condition
leftjoin - all records in left table. Null if there is no matching record on right table   
rightjoin - all records in right table
"""

