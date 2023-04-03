j = 0
list_temp=[]
import math

class Pagination:
    def __init__(self, items = [], pagesize = 10) -> None:
        global j
        self.items = items
        self.pagesize = pagesize
        self.totalpages = math.floor(len(self.items)/self.pagesize)
        # self.currentpage = j + 1
    def get_visible_items(self):
        list_temp=[]
        if j == math.floor(len(self.items)/self.pagesize):
            for i in range(self.pagesize * j, len(self.items)):
                list_temp.append(p.items[i])
        else:
            for i in range(self.pagesize * j, self.pagesize * (j+1)):
                list_temp.append(p.items[i])
        self.currentpage = j + 1
        print(list_temp)
    def next_page(self):
        global j
        if j < len(self.items)/self.pagesize:
            j += 1
    def prev_page(self):
        global j
        if j > 0:
            j -= 1
    def first_page(self):
        global j
        j = 0
    def last_page(self):
        global j
        j = math.floor(len(self.items)/self.pagesize)
    def go_to_page(self):
        global j
        page_num = int(input('Enter a page number: '))
        if page_num > math.floor(len(self.items)/self.pagesize):
            j = self.totalpages
        else:
            j = page_num


        


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.items)

p.get_visible_items()
p.next_page()
p.get_visible_items()
p.last_page()
p.get_visible_items()
p. go_to_page()
p.get_visible_items()
print (p.totalpages)
print(p.currentpage)
# list_temp=[]
# j = 0
# for i in range(p.pagesize * j, p.pagesize * (j+1)):
#     list_temp.append(p.items[i])
# print(list_temp)
