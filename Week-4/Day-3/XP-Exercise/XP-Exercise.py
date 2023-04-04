# #Exercise 1
# class Showcase:
#     ''' Input built-in function receives the value given by user. Int function transforms the object into an integer value, if possible. Abs function shows the distance of a number from zero (Thus, it always has a positive value)'''
        
# input_showcase = input('Enter a number: ')
# int_showcase = int(input_showcase)
# abs_showcase = abs(int_showcase)
# print(input_showcase, int_showcase, abs_showcase, Showcase.__doc__)

#Exercise 2 I didn't understand how to add two objects directly as we are required by the task condition, so I used int(object)
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'
    def __int__(self):
        return self.amount
    def __repr__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'
    def __add__(self, num):
        return self.amount + num
    def __iadd__(self, num):
        self.amount += num
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

try:
    c1 + int(c3)
    if c1.currency != c3.currency:
        raise TypeError
except TypeError:
    print(f'Cannot add between Currency type <{c1.currency}> and <{c3.currency}>')


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + int(c2))
print(c1)
c1 += 5
print(c1)
c1 += int(c2)
print(c1)
