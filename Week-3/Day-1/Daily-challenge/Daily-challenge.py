string = input('Enter you message. It must be 10 characters long ')
if len(string) > 10:
    print('Your message it too long')
elif len(string) < 10:
    print('Your string is too short')

print (string[0])
print (string[len(string) - 1]) #string[-1] also works

newstring = ''
for char in range(0, len(string)):
    newstring = newstring + string[char]
    print (newstring)

import random
lst = list(string)
random.shuffle(lst)
result = ''.join(lst)
print (result)

