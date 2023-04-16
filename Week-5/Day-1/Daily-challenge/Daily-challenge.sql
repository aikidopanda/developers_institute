create table actors (actor_id serial primary key, first_name varchar(50) not null, last_name varchar(100) not null, age date not null, number_oscars smallint not null)
insert into actors (first_name, last_name, age, number_oscars) values
('Jack', 'Nicholson', '04-22-1937', 3),
('Leonardo', 'DiCaprio', '11-11-1974', 1)
('Alfredo James', 'Pacino', '04-25-1940', 1);
select count (first_name) from actors;
insert into actors (first_name, last_name, age, number_oscars) values
('Noname', 'Noname', '06-10-1973') --will result in error