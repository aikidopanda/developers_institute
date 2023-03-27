# #Challenge 1

# number = int(input('Enter a number: '))
# length = int(input('Enter a length: '))

# for num in range(1, length + 1):
#     print(number * num)

#Challenge 2

user_string = input('Enter a string: ')

new_str =''
i = 0
j = 0

while j < len(user_string):
    if user_string[j] == user_string[i]:
        print('skipped')
        j += 1
    else:
        new_str += user_string[i]
        j += 1
        i = (j - 1)
if new_str[-1] != user_string[-1]:
    new_str += user_string[-1]
print(new_str) 


