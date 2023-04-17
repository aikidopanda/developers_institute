-- create table purchases (id serial primary key, customer_id smallint references customers(id), item_id smallint references items(id), quantity_purchased smallint);
-- insert into purchases(customer_id, item_id, quantity_purchased) values
-- ((select id from customers where fname = 'Scott' and lname = 'Scott'),
--  (select id from items where item = 'Fan'),
--  1);
-- insert into purchases(customer_id, item_id, quantity_purchased) values
-- ((select id from customers where fname = 'Melanie' and lname = 'Johnson'),
--  (select id from items where item = 'Large Desk'),
--  10);
-- insert into purchases(customer_id, item_id, quantity_purchased) values
-- ((select id from customers where fname = 'Greg' and lname = 'Jones'),
--  (select id from items where item = 'Small Desk'),
--  2);
select * from purchases;
select customer_id, item_id, quantity_purchased, fname, lname from purchases
inner join customers on purchases.customer_id = customers.id;
select * from purchases where customer_id = 5;
select * from purchases where item_id < 3;
select fname, lname, item_id, item from customers
left join purchases on customers.id = purchases.customer_id
left join items on purchases.item_id = items.id;
--I didn't understand the task number 3 so didnt complete it as well


