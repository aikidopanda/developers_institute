class Human:
    def __init__(self,id_number,name,age,priority,blood_type):
        self.id_number = id_number
        self.age = age
        self.name = name
        self.priority = priority
        self.blood_type = blood_type
        self.family = []
    def __repr__(self):
        return f'{self.name}'
    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)
    

class Queue:
    def __init__(self):
        self.humans = []
        
    def add_person(self,person):
        if person.age >= 60 or person.priority == True:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
    
    def find_in_queue(self,person):
        for i in range(len(self.humans)):
            if person == self.humans[i].name:
                return i
            
    def swap(self, person1, person2):
        index1 = self.humans.index(person1)
        index2 = self.humans.index(person2)
        self.humans[index1] = person2
        self.humans[index2] = person1

    def find_next(self):
        result = self.humans.pop(0)
        return result
    
    def find_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                result = self.humans.pop(i)
                return result
            
    def sort_by_age(self):
        self.humans.sort(key = lambda x: (x.priority, x.age), reverse = True)

    def rearrange_queue(self):
        for i in range(len(self.humans) - 1):
            if self.humans[i] in self.humans[i + 1].family and self.humans[i].priority == False and self.humans[i].age < 60:
                self.swap(self.humans[i],self.humans[i - 1])


#Testing
queue1 = Queue()
person1 = Human(456, 'Thomas', 34, False, 'A')
person2 = Human(512, 'Andrea', 52, False, 'A')
person3 = Human(243, 'George', 67, True, 'AB')
person4 = Human(54, 'Maria', 35, False, 'B')
person5 = Human(310, 'Alice', 31, True, 'O')
person3.add_family_member(person5)
queue1.add_person(person1)
queue1.add_person(person2)
queue1.add_person(person3)
queue1.add_person(person4)
queue1.add_person(person5)
# queue1.swap(person1, person2)
print(queue1.humans)
print(queue1.find_in_queue('Thomas'))
# print(queue1.find_next())
# print(queue1.find_next_blood_type('A'))
queue1.sort_by_age()
print(queue1.humans)
queue1.rearrange_queue()
print(queue1.humans)
