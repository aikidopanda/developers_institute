from collections import Counter
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
    pass #gonna do it later today if I have time, since this is bonus




text = Text('A good book would sometimes cost as much as a good house.')
print(Text.frequency(Text.from_ext_file(), 'French'))
print(Text.most_common(Text.from_ext_file()))
print(Text.unique_words(Text.from_ext_file()))

Text.from_ext_file()

