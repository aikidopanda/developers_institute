# #Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

merged = dict(zip(keys, values))

print (merged)

# #Exercise 2
family = {'Rick': 43, 'Beth': 13, 'morty': 5, 'summer': 8}
price = 0
for key in family:
    if family[key] > 12:
        price += 15
    elif family[key] >= 3:
        price += 10
print (f'Total cost of tickets:{price}') # this family should pay $50

#Bonus

family = {}
price = 0
while True:
    nameinput = input('Write your name or write quit when you bought all the needed tickets ')
    if nameinput == 'quit':
        break
    else:
        ageinput = int(input(f'Ok, write the age of {nameinput}: '))
        family[nameinput] = ageinput
for key in family:
    if family[key] > 12:
        price += 15
    elif family[key] >= 3:
        price += 10
print (f'Total cost of tickets:{price}')
print (family)

#Exercise 3
brand = {
    'name': 'Zara',
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']
    }
}
brand['number_stores'] = 2
print(brand['type_of_clothes'])
brand['country_creation'] = 'Spain'
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
for key in brand:
    print(key)
more_of_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand={**brand,**more_of_zara}
print (brand['number_stores']) #old value was overwritten since dictionaries had been merged

#Exercise 4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}
for num in range(len(users)):
    disney_users_A[users[num]] = num
print (disney_users_A)

disney_users_B = dict(enumerate(users))
print(disney_users_B)

users.sort()
disney_users_C = {}
for num in range(len(users)):
    disney_users_C[users[num]] = num
print(disney_users_C)

disney_users_A = {} # comment previous exercises before running this otherwise it gives incorrect results
for num in range(len(users)):
    if 'i' in users[num]:
        disney_users_A[users[num]] = num
print (disney_users_A)

disney_users_B = dict(enumerate(users))
print(disney_users_B)
for key in disney_users_B.copy():
    if disney_users_B[key][0] != 'M' and disney_users_B[key][0] != 'P':
        del disney_users_B[key]
print(disney_users_B)







