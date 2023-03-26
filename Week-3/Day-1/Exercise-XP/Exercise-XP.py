#Exercise 1
hello_world = 'Hello world '
print(hello_world + hello_world + hello_world + hello_world)
#Exercise2
print(99**3*8)
#Exercise 3
# false, true, false, error, false
#Exercise 4
computer_brand = "HP"
print('I have an {} computer'.format(computer_brand))
#Exercise 5
name = 'Alexey'
age = 34
shoe_size = 41
info = 'My name is {}, I am {} and my shoe size is {}. Not very interesting, tbh'.format(name,age,shoe_size)
print(info)
#Exercise 6
a = 2
b = 7
if a > b:
    print('Hello World')
else:
    print('a is not greater than b')
#Exercise 7
num = input('Enter a number: ')
num_1 = int(num)
if num_1 % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')
#Exercise 8
your_name = input('Enter your name: ')
my_name = 'Alex'
if your_name == my_name:
    print('Wow! You have the same name!')
#Exercise 9
height_inch= input('Enter your height: ')
height_cm = float(height_inch) * 2.54
if height_cm > 145:
    print('You are tall enough to ride!')
else:
    print('You cannot ride, you need to grow some more')




    