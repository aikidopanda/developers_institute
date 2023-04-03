#Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    all_cats = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Cat.all_cats.append(name)

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

lucky = Bengal('Lucky', 5)
tappy = Chartreux('Tappy', 9)
maroo = Siamese('Maroo', 8)

sara_pets = Pets(Cat.all_cats)

print (Cat.all_cats)

print(Cat.walk(lucky))
print(Cat.walk(tappy))
print(Cat.walk(maroo))

#Exercise 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f'{self.name} is barking')
    def run_speed(self):
        return self.weight/self.age * 10
    def fight(self, other_dog):
        if self.weight * self.run_speed() > other_dog.weight * other_dog.run_speed():
            return f'{self.name} won!'
        else:
            return f'{other_dog.name} won!'

rex = Dog('Rex', 7, 15)
torres = Dog('Torres', 5,18)
jimmy = Dog('Jimmy', 9, 15)

#Testing that everything works
rex.bark()
print(jimmy.run_speed())
print(torres.fight(rex))

#Exercise 3

            


