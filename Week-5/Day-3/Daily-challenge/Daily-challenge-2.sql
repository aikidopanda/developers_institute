create table orders (order_id serial primary key, item_id int references items(id), user_id smallint , quantity smallint);
insert into orders (item_id, user_id, quantity) values
((select id from items where item = 'Large Desk'), 3, 5)
((select id from items where item = 'Small Desk'), 3, 2),
((select id from items where item = 'Fan'), 3, 6)
create or replace function total_price(order int)
returns int as $$
declare total_sum int;
	begin
		total_sum := (select sum(quantity * price) from orders join items on orders.item_id = items.id where orders.order_id = order); 
		return total_sum;
	end;
$$ language plpgsql;
select * from total_price(3)
create or replace function total_price_for_user(order int, uid int)
returns int as $$
declare total_sum int;
	begin
		total_sum := (select sum(quantity * price) from orders join items on orders.item_id = items.id join customers on customers.id = uid where orders.order_id = order); 
		return total_sum;
	end;
$$ language plpgsql;
select * from total_price_for_user(2,3)
