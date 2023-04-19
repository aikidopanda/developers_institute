import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '#'
DATABASE = 'Home'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)
# cursor = connection.cursor()


class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}, costs {self.price}'

    def save(self):
        query = f"insert into menu (name, price) values ('{self.name}', {self.price})"
        with connection.cursor() as cursor:     
            cursor.execute(query)
                # result = cursor.fetchall()
                # return result
            connection.commit()

    # Changed delete and update functionality because restaurant managers doesnt need to enter objects, he knows just name and price of each item
    
    def delete(name):
        query = f"delete from menu where name = '{name}'"
        with connection.cursor() as cursor: 
            cursor.execute(query)
            connection.commit()

    def update(name, prevname, price):
        query = f"update menu set name = '{name}', price = {price} where name = '{prevname}'"
        with connection.cursor() as cursor: 
            cursor.execute(query)
            connection.commit()

    @classmethod
    def all(cls):
        query = 'select * from menu'
        with connection.cursor() as cursor: 
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def get_by_name(name):
        query = f"select * from menu where name = '{name}'"
        with connection.cursor() as cursor: 
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result
            else:
                return None

#Testing
# item = MenuItem('Burger', 35)
# item.save()
# MenuItem.update('Veggie Burger', 'Burger', 37)
# item.name = 'Veggie Burger'
# MenuItem.delete('Veggie Burger')
# item2 = MenuItem.get_by_name('Beef Stew')
# items = MenuItem.all()
# print(item2)
# print(items)
