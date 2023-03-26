#Exercise 3
# true, true, false, false, true, false,  

#Exercise 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print (len(my_text))

#Exercise 5
a_used = False
maxcounter = 0
while a_used == False:
    sentence = input('Enter the longest sentence you can write without using the A letter  ')
    counter = 0
    for char in sentence:
        if char == 'a' or char == 'A':
            a_used == True
            maxcounter = 0
            print ('You lost! Your record has be set to {}'.format(maxcounter))
            break
        else:
            counter = counter + 1
            if counter > maxcounter:
                print('Congratulations! Your record now is {}'.format(maxcounter))
                maxcounter = counter
        
        


