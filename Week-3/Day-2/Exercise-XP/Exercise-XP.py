#Exercise 1

my_fav_numbers = { 4, 7, 17, 24 }
my_fav_numbers.add(28)
my_fav_numbers.add(35)
my_fav_numbers_list = list(my_fav_numbers)
my_fav_numbers_list.pop()
my_fav_numbers = set(my_fav_numbers_list)
print('My favourite numbers: {}'.format(my_fav_numbers))

friend_fav_numbers = {3 ,7 ,19, 31}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print('Our favourite numbers: {}'.format(our_fav_numbers))