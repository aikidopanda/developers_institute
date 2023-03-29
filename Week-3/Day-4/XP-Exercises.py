import random
# #Exercise 1
# def display_message():
#     print('I am learning here!')

# display_message()

# #Exercise 2
# def favorite_book(title):
#     print(f'My favorite book is {title}')

# userbook = input('Tell me what is your favourite book')
# favorite_book(userbook)

# #Exercise 3
# def describe_city(city, country = 'Israel'):
#     print(f'The {city} is in {country}')

# usercity = input('Enter a city: ')

# describe_city(usercity, usercountry)

#Exercise 4
# import random
# def random_num(num1, num2):

#     if num1 < 0 or num1 > 100:
#         print('Invalid number. Enter a number between 0 and 100 ')
#         return False
#     elif num1 == num2:
#         print('Critical success!')
#     else:
#         print('You were unlucky. Try again')
#     print(num1, num2)

# usernum1 = int(input('Enter a number between 0 and 100 '))
# usernum2 = random.randint(0,100)
# random_num(usernum1, usernum2)

# #Exercise 5
# def make_shirt(size = 'L', text = 'I love Python' ):
#     print(f'The size of a shirt is {size} and the text is {text}')

# result1 = make_shirt()
# result2 = make_shirt('M',)
# result3 = make_shirt('S','The Cure')

# #Exercise 6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(lst):
#     for i in range(len(lst)):
#         print (lst[i])

# show_magicians(magician_names)

# def make_great(lst):
#     for i in range(len(lst)):
#         lst[i] += ' The Great'

# make_great(magician_names)

# show_magicians(magician_names)

#Exercise 7
import random
def get_random_temp(season):
    if season == 'winter':
        return random.uniform(-10,16)
    elif season == 'spring' or season == 'autumn':
        return random.uniform(0,23)
    elif season == 'summer':
        return random.uniform(15,40)

def main():
    season_input = input('Please tell me what season is today: ')
    temp = get_random_temp(season_input)
    if temp < 0:
        print(f'The temperature now is {temp} degress Celsius. Wear something warm today')
    elif temp < 16:
        print(f'The temperature now is {temp} degress Celsius. Dont forget your jacket')
    elif temp < 23:
        print(f'The temperature now is {temp} degress Celsius. Just fine for being outdoors')
    elif temp < 32:
        print(f'The temperature now is {temp} degress Celsius. Dont stay long under the sun')
    else:
        print(f'The temperature now is {temp} degress Celsius. Better stay at home and turn the air conditioner on')

main()

    





    


