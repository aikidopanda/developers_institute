create table items (id serial primary key, item varchar (10), price int)
create table customers(id serial primary key, fname varchar(10), lname varchar(10))

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where lname = 'Smith'; -- will be empty
select * from customers where lname = 'Jones';
select * from customers where fname != 'Scott'