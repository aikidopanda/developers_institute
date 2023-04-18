-- select name from language;
-- select title, description, language from film
-- join language on film.language_id = language.language_id;
-- -- there are no films without a language in the database, they all have English, so the task to fetch films wihout a language can't be completed
-- select language.language_id, name, title from language
-- left join film on language.language_id = film.language_id;
-- create table new_films
-- (
-- id serial primary key,
-- name text not null
-- );
-- insert into new_films (name) values
-- ('Everything Everywhere All at Once'),
-- ('Dead dont die'),
-- ('Once Upon a Time in Hollywood')
-- ;
-- create table customer_review (
-- review_id serial primary key,
-- film_id int,
-- language_id int references language(language_id),
-- title varchar(50),
-- score int,
-- check(score > 0 and score < 11),
-- review_text text,
-- last_update timestamp not null default current_timestamp,
-- foreign key (film_id) references new_films(id) on delete cascade
-- );
-- insert into customer_review (film_id, language_id, score, review_text) values
-- (1, 1, 5, 'The film is a complete mess I didnt understand a thing'),
-- (2, 6, 10, 'Dieser film ist Grandios!');
-- delete from new_films where name = 'Everything Everywhere All at Once';
--the customer reviews on that film should also be deleted

--Exercise 2
-- update film set language_id = 5 where film_id = 33 or film_id = 35;

--the customer_address_id_fkey is referencing address_id column in the address table. When this column in address table gets updated, the address_id in customers table gets updated as well
-- the on delete restrict entry says that if address_id in the address table is deleted, the address_id in customers table will keep its place.

-- drop table customer_review; --no additional checking is required

select count(rental_id) from rental where return_date is null;

select rental.inventory_id, film.title, film.rental_rate from rental
join inventory on rental.inventory_id = inventory.inventory_id and return_date is null
join film on inventory.film_id = film.film_id order by film.rental_rate desc limit 30;

select first_name, last_name, film.title, film.description, film.film_id from actor
join film_actor on actor.actor_id = film_actor.actor_id 
join film on film_actor.film_id = film.film_id where first_name = 'Penelope' and last_name = 'Monroe' and film.description like '%Sumo%';

select category_id, title, description, length, rating from film_category 
join film on film_category.film_id = film.film_id where category_id = 6 and film.length < 60 and film.rating = 'R';

select customer.customer_id, first_name, last_name, film.film_id, title, rental_rate from customer
join rental on customer.customer_id = rental.customer_id
join inventory on rental.inventory_id = inventory.inventory_id 
join film on inventory.film_id = film.film_id where first_name = 'Matthew' and last_name = 'Mahan' and rental.return_date > '2005-07-28' and rental.return_date < '2005-08-01' and film.rental_rate >= 4.00;

select customer.customer_id, first_name, last_name, film.film_id, title, replacement_cost from customer
join rental on customer.customer_id = rental.customer_id
join inventory on rental.inventory_id = inventory.inventory_id 
join film on inventory.film_id = film.film_id where first_name = 'Matthew' and last_name = 'Mahan' and (film.description like '%Boat%' or film.title like '%Boat%') order by replacement_cost desc;