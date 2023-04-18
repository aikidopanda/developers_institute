-- create table customer (id serial primary key, first_name text not null, last_name text not null);

-- create table customer_profile (
-- 	id serial primary key, 
-- 	is_logged_in boolean default false, 
-- 	customer_id int unique not null,
-- 	foreign key (customer_id) references customer(id)
-- );

-- insert into customer (first_name, last_name) values
-- 	('John', 'Doe'),
-- 	('Jerome', 'Lalu'),
-- 	('Lea', 'Rive');

-- insert into customer_profile (is_logged_in, customer_id) values
-- (true, (select id from customer where first_name = 'John')),
-- (false, (select id from customer where first_name = 'Jerome'));

-- select first_name from customer
-- join customer_profile on customer.id = customer_profile.customer_id where is_logged_in = true;

-- select first_name, is_logged_in from customer
-- left join customer_profile on customer.id = customer_profile.customer_id;

-- select count(first_name) from customer
-- left join customer_profile on customer.id = customer_profile.customer_id where is_logged_in = false;

-- create table book (book_id serial primary key, title text not null, author varchar(100) not null);

-- insert into book (title, author) values
-- ('Alice in Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K.Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student (
-- 	student_id serial primary key,
-- 	name varchar(100) not null unique,
-- 	age smallint,
-- 	check (age <= 15)
-- );

-- insert into student (name, age) values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table library(
-- 	book_fk_id int,
-- 	student_id int,
-- 	borrowed_date timestamp default current_timestamp,
-- 	foreign key (book_fk_id) references book(book_id) on delete cascade on update cascade,
-- 	foreign key (student_id) references student(student_id) on delete cascade on update cascade	
-- );

-- alter table library alter column borrowed_date type date;

-- insert into library(book_fk_id, student_id, borrowed_date) values
-- ((select book_id from book where title = 'Alice in Wonderland'), 
--  (select student_id from student where name = 'John'),
-- '2022-02-15'),
-- ((select book_id from book where title = 'To kill a mockingbird'), 
--  (select student_id from student where name = 'Bob'),
-- '2021-03-03'),
-- ((select book_id from book where title = 'Alice in Wonderland'), 
--  (select student_id from student where name = 'Lera'),
-- '2021-05-23'),
-- ((select book_id from book where title = 'Harry Potter'), 
--  (select student_id from student where name = 'Bob'),
-- '2021-08-21');

-- select * from library;

-- select name, title from student
-- join library on student.student_id = library.student_id
-- join book on library.book_fk_id = book.book_id;

-- select avg(age) from student
-- join library on student.student_id = library.student_id where library.book_fk_id = (select book_id from book where title = 'Alice in Wonderland');

-- delete from student where name = 'Bob';
-- every entry about Bob taking books will be also deleted



