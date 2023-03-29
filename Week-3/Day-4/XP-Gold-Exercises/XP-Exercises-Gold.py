#Exercise 1
# current_year = 2023
# current_month = 3

# def get_age(year, month, day = 1):
#     age = (current_year - year)
#     if current_month < month:
#         age -= 1
#     return age

# def can_retire(gender, birth_date):

#     list_temp = birth_date.split('/')

#     user_year = int(list_temp[0])
#     user_month = int(list_temp[1])
#     user_day = int(list_temp[2])

#     user_age = get_age(user_year, user_month, user_day)

#     if user_age >= 67 and gender == 'M':
#         return True# print('You can retire')
#     elif user_age >= 62 and user_gender == 'F':
#         return True# print ('You can retire')
#     else:
#         return False# print('You can not retire yet')

# user_gender = input('Enter your gender: (M or F): ')
# user_birth_date = input('Enter your birthdate (YYYY/MM/DD:) ')  
# print(can_retire(user_gender, user_birth_date))

#Exercise 2 done in class

import random
def throw_dice():
    return random.randint(1,6)

def throw_until_doubles(): 

    attempts = 0

    while True:
        dice_1 = throw_dice()
        dice_2 = throw_dice()
        print([dice_1,dice_2])
        if dice_1 == dice_2:
            return attempts
            break
        else:
            attempts += 1
# print(throw_until_doubles())

def main():
    i = 1
    collection = []
    sum = 0
    while i <= 100:
        result = throw_until_doubles()
        collection.append(result)
        sum += result
        i += 1
    avg = sum/100
    avg = round(avg,2)
    # print(f'All throws: {collection}, Total throws: {sum}, Average throws to make double:{avg}')
    return collection, sum, avg
print (main())




