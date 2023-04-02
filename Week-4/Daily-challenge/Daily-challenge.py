class Farm:
    animals = {}
    def __init__(self, name):
        self.name = name
    def add_animal(animal,count = 1):
        if animal in Farm.animals:
            Farm.animals[animal] += count
        else:
            Farm.animals.update({animal: count})
    def get_info():
        info = ''
        for k in Farm.animals:
            info = info + k + ' : ' + str(Farm.animals[k]) + '\n'
            fullinfo = 'McDonalds Farm\n\n' + info + '\n' + '   E-I-E-I-O!'
        return fullinfo
    def get_animal_types():
        animal_list = []
        for k in Farm.animals:
            animal_list.append(k)
        return sorted(animal_list)
            

macdonald = Farm("McDonald")
Farm.add_animal('cow', 5)
Farm.add_animal('sheep')
Farm.add_animal('sheep')
Farm.add_animal('goat', 12)
print(Farm.get_info())
print(Farm.get_animal_types())


            