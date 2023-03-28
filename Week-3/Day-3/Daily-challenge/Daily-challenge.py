# #Challenge 1

user_word = input('Enter a word: ')
dict = {}
for num in range(len(user_word)):
   dict.update({user_word[num]: []})
for num in range(len(user_word)):
   dict[user_word[num]].append(num)
print (dict)

#Challenge 2

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet ='$1500'

for key in items_purchase:
    list_temp = list(items_purchase[key])
    list_temp.remove('$')
    if ',' in items_purchase[key]:
        list_temp.remove(',')
    items_purchase[key] = ''.join(list_temp)
    items_purchase[key] = int(items_purchase[key])
    print(items_purchase[key])

list_temp = list(wallet)
list_temp.remove('$')
wallet = ''.join(list_temp)
wallet = int(wallet)



can_buy = []

for key in items_purchase:
    if items_purchase[key] < wallet:
        can_buy.append(key)
    else:
        continue

if len(can_buy) > 0:
    print (f'You can afford: {can_buy}')
else:
    print ('You dont have enough money to buy anything in this store:(')




