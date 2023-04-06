#import gensim # I have a 'ModuleNotFoundError: No module named 'gensim'' error so can't check if my code works:( i have installed and reinstalled mumpy and gensim over 9000 times
from collections import Counter
import string
class Text:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return 'this text'
    def frequency(self, word):
        list_temp = self.text.split()
        if list_temp.count(word) > 0:
            return f'There are {list_temp.count(word)} occurences of {word} in {self}'
        else:
            return None
    def most_common(self):
        list_temp = self.text.split()
        counter = Counter(list_temp)
        return counter.most_common(1)
    def unique_words(self):
        list_temp = self.text.split()
        set_temp = set(list_temp)
        list_temp2 = list(set_temp)
        return list_temp2
    @classmethod
    def from_ext_file(cls):
        with open ('the_stranger.txt', 'r') as file:
            text_ext = Text(file.read())
            return text_ext
        
class TextModification(Text):
    def remove_punctuation(self):
        modified_text = self.text.translate(str.maketrans('','',string.punctuation))
        return modified_text
    # def remove_all_stopwords(self):
    #     modified_text = remove_stopwords(self.text)
    #     return modified_text
    def remove_special(self):
        modified_text = ''.join(ch for ch in self.text if ch.isalnum())
        return modified_text
        




text = Text('A good book would sometimes cost as much as a good house.')
# print(Text.frequency(Text.from_ext_file(), 'French'))
# print(Text.most_common(Text.from_ext_file()))
# print(Text.unique_words(Text.from_ext_file()))
# print(TextModification.remove_punctuation(Text.from_ext_file()))
# # print(TextModification.remove_all_stopwords(Text.from_ext_file()))
print(TextModification.remove_special(Text.from_ext_file()))

Text.from_ext_file()


