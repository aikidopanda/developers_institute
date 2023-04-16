create table items (id serial primary key, item varchar, price int)
create table customers(id serial primary key, fname varchar, lname varchar)

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where lname = 'Smith'; -- will be empty
select * from customers where lname = 'Jones';
select * from customers where fname != 'Scott'