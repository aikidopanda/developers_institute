select * from customer;

select first_name || ' ' || last_name as full_name from customer;

select distinct create_date from customer; 

select * from customer order by first_name desc;

select film_id, title, description, release_year, rental_rate from film order by rental_rate;

select address, phone from address where district='Texas';

select * from film where film_id = 15 or film_id = 150;

select film_id, title, description, length, rental_rate from film where title = 'Dead man';

select film_id, title, description, length, rental_rate from film where title like 'De%';

select * from film order by rental_rate,film_id limit 10;

select * from film order by rental_rate,film_id limit 10 offset 10;

select first_name, last_name, amount, payment_date from customer
inner join payment on customer.customer_id = payment.customer_id;

select title from film left join inventory on inventory.film_id = film.film_id where inventory.film_id is null;

select city, country from city left join country on city.country_id = country.country_id;

select customer.customer_id, first_name, last_name, staff_id, amount, payment_date from customer left join payment on customer.customer_id = payment.customer_id order by payment.staff_id;



