import sys
from XP_Exercise import *

def load_manager():
    item_name = input('Please enter a new item name: ')
    item_price = input('And its price: ')
    return MenuItem(item_name, item_price)

def show_user_menu():
    user_option = input('Choose an option:\n V - View the menu\n A - Add an item to the menu\n U - update the existing item\n D - delete an item\n F - find an item in menu\n X - exit\n')
    if user_option.upper() == 'V':
        show_restaurant_menu()
    elif user_option.upper() == 'A':
        add_item_to_menu()
    elif user_option.upper() == 'U':
        update_item()
    elif user_option.upper() == 'D':
        remove_item_from_menu()
    elif user_option.upper() == 'F':
        item_to_find = input('Enter an item name to find in menu:')
        print(MenuItem.get_by_name(item_to_find))
    elif user_option.upper() == 'X':
        show_restaurant_menu()
        sys.exit()
    else:
        print('Invalid input! Please see the valid buttons')
    show_user_menu()
       
def add_item_to_menu():
    add_option = load_manager()
    add_option.save()
    if add_option.get_by_name != None:
        print('Item successfully added!')

def update_item():
    prev_name = input('Enter the name of menu item where you want to change name or ptice: ')
    new_name = input('Enter the new name: ')
    price = input('Enter the price, whether it was changed or not: ')
    MenuItem.update(new_name, prev_name, price)


def remove_item_from_menu():
    del_option = input('Enter menu item to delete: ')
    MenuItem.delete(del_option)
    if MenuItem.get_by_name(del_option) == None:
        print('Item successfully removed!')

def show_restaurant_menu():
    print(MenuItem.all())

show_user_menu()

# cursor.close()
# connection.close()