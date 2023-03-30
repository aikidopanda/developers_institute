#simple way, without using list comprehension. It works however

def sorting_function(message):
    message = message.split(',')
    # return sorted(message)
    message = sorted(message)
    message = ','.join(message)
    return message

user_message = input('Enter a list of words, separated by a comma (dont use spaces). My function will sort them alphabetically ')
print(sorting_function(user_message))



