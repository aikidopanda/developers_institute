import random
# #Exercise 1
# class Documentation:
#     ''' This code allows to generate random sentences from a large word list, both upper and lower cases. The length of the desired sentence should be between 2 and 20'''
# import random
# def get_words_from_file():
#     with open('words.txt', 'r') as file:
#         wordstr = file.read()
#         word_list = wordstr.split('\n')
#         return word_list

# def get_random_sentence(length):
#     word_list = get_words_from_file()
#     my_sentence = ''
#     for _ in range(length):
#         my_sentence += random.choice(word_list) + ' '
#     return my_sentence
# # print(get_random_sentence(5))

# def get_random_sentence_lower(length):
#     word_list = get_words_from_file()
#     my_sentence = ''
#     for _ in range(length):
#         my_sentence += random.choice(word_list) + ' '
#     return my_sentence.lower()
# # print(get_random_sentence_lower(7))

# def main():
#     print(Documentation.__doc__)
#     user_inp = int(input('Enter a length of a random sentence you want to generate '))
#     if user_inp < 2 or user_inp > 20:
#         raise Exception('The lenght of sentence should be between 2 and 20!')
#     else:
#         print(get_random_sentence(user_inp))
#         print(get_random_sentence_lower(user_inp))
# main()

#Exercise 2
import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
print(sampleJson['company']['employee']['payable']['salary'])
sampleJson['company']['employee']['birth_date'] = '05 December 1988'
print(sampleJson)

json_file = 'samplejson.json'
with open (json_file, 'w') as sample:
    json.dump(sampleJson, sample)





