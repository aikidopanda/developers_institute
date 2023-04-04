#Exercise 1 - see exercise-one.py and func.py, I had to create them due to the task condition

#Exercise 2

import random

# def randomizer(num):
#     random_num = random.randint(1,100)
#     if num == random_num:
#         print(f'Success! The {num} is equal to {random_num}')
#     else:
#         print(f'{num} and {random_num} are not equal, try again')

# user_num = int(input('Enter a number from 1 to 100: '))
# randomizer(user_num)

#Exercise 3
import string
chars = string.ascii_letters
length = 5
mystr = ''
for i in range(length):
    mystr += random.choice(chars)
print(mystr)

#Exercise 4
from datetime import date
# def currentdate():
#     return date.today()

# print(f'Today is {currentdate()}')

#Exercise 5

import datetime

# def days_until_new_year():
#     current_time = datetime.datetime.now()
#     date2 = datetime.datetime(2024, 1, 1)

#     delta = date2 - current_time
#     return delta


# print(f'There are {days_until_new_year()} until January 1')

#Exercise 6

# def minutes_i_live(birthday):
#     birth_date = datetime.datetime.strptime(birthday, "%d %B %Y")
#     current_time = datetime.datetime.now()
#     delta = current_time - birth_date
#     return delta.total_seconds()/60

# user_input = input('Enter your birthday in format day month year' )

# print(f'You live {minutes_i_live(user_input)} minutes')

#Exercise 7

# def currentdate_holiday():

#     current_day = datetime.date.today()
#     current_time = datetime.datetime.now()
#     holiday_name = 'Pesach'
#     holiday_date = datetime.datetime(2023,4,11) # the end of Pesach week, didnt enter the beginning of it since its tomorrow
#     print(f'Today is {current_day}.The next holiday is {holiday_name} and it its in {holiday_date - current_time}')

# currentdate_holiday()

#Exercise 8

# def seconds_i_live(birthday):
#     birth_date = datetime.datetime.strptime(birthday, "%d %B %Y")
#     current_time = datetime.datetime.now()
#     delta = current_time - birth_date
#     return delta.total_seconds()

# my_seconds = seconds_i_live('5 december 1988')
# my_days = seconds_i_live('5 december 1988')/86400 # theres 86400 seconds in one day

# print(f'I am {my_seconds} seconds and {my_days} days old')

# #planets_data
# earth_year = 365.25
# planet_name = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# planet_year = [0.2408467, 0.61519726, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132]
# planet_year2 = []
# for i in range(len(planet_year)): # getting the length of the year on each planet
#     planet_year2.append(earth_year * planet_year[i])
# print(planet_year2)
# for i in range(len(planet_year2)):
#     my_age_on_this_planet = my_days/planet_year2[i]
#     print(f'I would be {my_age_on_this_planet} years old on {planet_name[i]}')

#Exercise 9

from faker import Faker
import itertools
fake = Faker()

def create_list_dict(n):
    return list(itertools.repeat({}, n))

users = create_list_dict(15)

for i in range(len(users)):
    users[i] = {
        'name': fake.name(),
        'address': fake.address(),
        'language code': fake.language_code()
    }
print(users)









