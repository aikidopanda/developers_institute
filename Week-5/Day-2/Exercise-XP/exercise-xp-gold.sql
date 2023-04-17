select count(title), rating from film group by rating;
select * from film where (rating = 'G' or rating = 'PG-13')
and length < 120 and rental_rate < 3.00 order by title;
update customer set first_name = 'Alexey', last_name = 'Soroker', email = 'sample@gmail.com', last_update = '2023-04-17 14:49:45.738' where customer_id = 315;
update address set address = 'Khaviva Reek 53', district = 'Haifa', phone = '053-1111111', last_update = '2023-04-17 14:49:45.738' where address_id = 315;