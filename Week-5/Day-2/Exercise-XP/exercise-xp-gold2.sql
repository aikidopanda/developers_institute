-- update students set birth_date = '11/02/1998' where last_name = 'Benichou';
-- update students set last_name = 'Guez' where last_name = 'Grez';
-- delete from students where first_name = 'Lea' and last_name = 'Benichou';
-- select count(id) from students;
-- select count(id) from students where birth_date > '01/01/2000';
-- update students set math_grade = 80 where id = 1;
-- update students set math_grade = 90 where id = 2 or id = 4;
-- update students set math_grade = 40 where id = 6;
-- select count(first_name) from students where math_grade > 83;
-- insert into students(last_name, first_name, birth_date, math_grade) values
-- ('Simpson', 'Omer', '1980-10-03', 70);
select count(math_grade), last_name, first_name from students group by last_name, first_name;
select sum(math_grade), last_name, first_name from students group by last_name, first_name;
select sum(math_grade) from students;

