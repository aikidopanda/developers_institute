class Anagram_checker:
    def __init__(self):
        with open('sowpods.txt') as file:
            self.text = file.readlines()
    def is_valid_word(word):
        valid = True
        for i in range(len(word)):
            if word[i].isalpha() == False:
                valid = False
        return valid
    def get_anagrams(self,word):
        word_list = [item.strip() for item in self.text]
        anagrams_list = []
        for i in range(len(word_list)):
            if Anagram_checker.is_anagram(word,word_list[i]) == True:
                anagrams_list.append(word_list[i])
        return anagrams_list
    def is_anagram(word1, word2):
        if word1.lower() != word2.lower() and sorted(word1.lower()) == sorted(word2.lower()):
            return True
        else:
            return False
        
# print(Anagram_checker.is_anagram('mate','MATE'))
# with open('sowpods.txt') as file:
#     text = file.readlines()
#     word_list = [item.strip() for item in text]
#     print(word_list)


        
        