class Family:
    def __init__(self, members, last_name):
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}    
        ]
        self.last_name = last_name
    def born(self):
        self.members.append(
            {
            'name': 'Jonathan',
            'age': 0,
            'gender': 'male',
            'is_child': True
            }
        )
        print('Congratulations! You have a new family member')
    def is_18 (self, name):
        for i in range(len(self.members)):
            if self.members[i]['name'] == name:
                if self.members[i]['age'] >= 18:
                    return True
                else:
                    return False
    def family_presentation(self):
        family_members = ''
        for i in range(len(self.members)):
            if i < len(self.members) - 1:
                family_members = family_members + self.members[i]['name'] + ', '
            else:
                family_members = family_members + self.members[i]['name'] + '.'
        print (f'This is a {self.last_name} family. Its members are: {family_members}')
        
        

jason = Family([], 'Jason')
Family.born(jason)

print(Family.is_18(jason, 'Michael'))
print(Family.is_18(jason, 'Jonathan'))
jason.family_presentation()
        
    