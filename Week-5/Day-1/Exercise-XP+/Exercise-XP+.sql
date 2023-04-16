create table students (id serial primary key, last_name varchar (20), first_name varchar (20), birth_date date)
insert into students (last_name, first_name, birth_date) values
('Benichou', 'Mark', '11/02/1998'),
('Cohen', 'Yoan', '12/03/2010'),
('Benichou', 'Lea', '07/27/1987'),
('Dux', 'Amelia', '04/07/1996'),
('Grez', 'David', '06/14/2003'),
('Simpson', 'Omer', '10/03/1980'),
('Soroker', 'Alex', '12/05/1988');
select * from students;
select * from students where last_name = 'Benichou' and first_name = 'Mark';
select * from students where last_name = 'Benichou' or first_name = 'Mark';
select * from students where first_name like '%a%' or first_name like '%A%';
select * from students where first_name like 'A%';
select * from students where first_name like '%a';
select * from students where substring(reverse(first_name), 2, 1) = 'a';
select * from students where id = 1 or id = 3;
select * from students where id = 1 and id = 3;
select * from students where birth_date >= '01-01-2000'