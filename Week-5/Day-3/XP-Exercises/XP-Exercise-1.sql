select name from language;
select title, description, language from film
join language on film.language_id = language.language_id;
-- there are no films without a language in the database, they all have English, so the task to fetch films wihout a language can't be completed

select language.language_id, name, title from language
left join film on language.language_id = film.language_id;

create table new_films
(
id serial primary key,
name text not null
);

insert into new_films (name) values
('Everything Everywhere All at Once'),
('Dead dont die'),
('Once Upon a Time in Hollywood')
;

create table customer_review (
review_id serial primary key,
film_id int,
language_id int references language(language_id),
title varchar(50),
score int,
check(score > 0 and score < 11),
review_text text,
last_update timestamp not null default current_timestamp,
foreign key (film_id) references new_films(id) on delete cascade
);

insert into customer_review (film_id, language_id, score, review_text) values
(1, 1, 5, 'The film is a complete mess I didnt understand a thing'),
(2, 6, 10, 'Dieser film ist Grandios!');

delete from new_films where name = 'Everything Everywhere All at Once';
the customer reviews on that film should also be deleted
