one_line = 'Hello world ' * 4 + 'I love Python ' * 4
print (one_line)

month = int(input('Enter a month number '))
if month >= 3 and month <= 5:
    print('Its Spring')
elif month >= 6 and month <= 8:
    print('Its Summer')
elif month >= 9 and month <= 11:
    print ('Its Autumn')
elif month <= 2 or month == 12:
    print ('Its Winter')
else:
    print('Theres no month with such number')


