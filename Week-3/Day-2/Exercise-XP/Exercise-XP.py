# #Exercise 1

# my_fav_numbers = { 4, 7, 17, 24 }
# my_fav_numbers.add(28)
# my_fav_numbers.add(35)
# my_fav_numbers_list = list(my_fav_numbers)
# my_fav_numbers_list.pop()
# my_fav_numbers = set(my_fav_numbers_list)
# print(f'My favourite numbers: {my_fav_numbers}')

# friend_fav_numbers = {3 ,7 ,19, 31}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(f'Our favourite numbers: {our_fav_numbers}')

# #Exercise 2 It is possible via converting tuple into a list, adding new item to a list and then converting again
# my_tuple  = (3, 5, 7, 8)
# my_tuple_list = list(my_tuple)
# my_tuple_list.insert(4,9)
# my_tuple = tuple(my_tuple_list)
# print(f'Converted tuple: {my_tuple}')

# #Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove('Banana')
# basket.remove('Blueberries')
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# basket.count('Apples')
# basket.clear()
# print(basket)

# #Exercise 4
# # 1. Float can contain decimal/non-integer values
# # 2. Didn't understand the question:( It seems to me that sequence of floats can be built the same way as the sequence of integers
# float_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# #or more complicated way
# float_list = []
# for num in range(3,11):
#     float_list.append(num/2)
# print(float_list)

# #Exercise 5
# for num in range(1, 21):
#     print (num)

# for num in range(1, 21):
#     if num%2 == 0:
#         print (num)

# #Exercise 6
# user_name=''
# while user_name != 'Alex':
#     user_name = input('Please enter your name ')
#     continue
# print('I have the same name!')

# #Exercise 7
# user_fav_fruits = input('Enter your favourite fruits. Separate them by space ')
# user_fav_fruits_list = user_fav_fruits.split()
# fruit = input('Choose a fruit ')
# if fruit in user_fav_fruits_list:
#     print('You have chosen one of your favourite fruits!')
# else:
#     print('You chose a new fruit. I hope you enjoy')

#Exercise 8
# user_order =''
# price = 10
# toppings = []
# while user_order != 'quit':
#     user_order = input('Add topping for your pizza: ')
#     if user_order == 'quit':
#         break
#     else:
#         print(f'You have added {user_order}!')
#         toppings.append(user_order)
#         price += 2.5
# print(f'You have chosen {toppings}! Your pizza costs {price}')

# #Exercise 9
# family_ages = input('Enter the age of each family member who needs a ticket, separated by space')
# family_ages_list = family_ages.split()
# price = 0
# for num in range(0,len(family_ages_list)):
#     if int(family_ages_list[num]) > 12:
#         price += 15
#     elif int(family_ages_list[num]) >= 3:
#         price += 10
# print (f'Total cost of tickets:{price}')


# teen_names = ['John', 'Alice', 'Thomas', 'Helen', 'Michael']
# teen_ages = ''
# teen_names_prohibited = []
# for num in range (0,len(teen_names)):
#     teen_ages = input(f'Enter the age of {teen_names[num]}')
#     if 16 <= int(teen_ages) <= 21:
#         teen_names_prohibited.append(teen_names[num])
        
# for num in range(0,len(teen_names_prohibited)):
#     if teen_names_prohibited[num] in teen_names:
#         teen_names.remove(teen_names_prohibited[num])

# print(f'Allowed for this film: {teen_names}')

# #Exercise 10
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = []

# while len(sandwich_orders) > 0:
#     finished_sandwiches.append(sandwich_orders[0])
#     sandwich_orders.pop(0)

# for num in range(0, len(finished_sandwiches)):
#     print(f'I made your {finished_sandwiches[num]}')

#Exercise 11
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print('The deli has ran out of pastrami')
while sandwich_orders.count('Pastrami sandwich') > 0:
    sandwich_orders.remove('Pastrami sandwich')

while len(sandwich_orders) > 0:
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.pop(0)

for num in range(0, len(finished_sandwiches)):
    print(f'I made your {finished_sandwiches[num]}')








    






