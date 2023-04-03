from XP_Exercises import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained):
        self.trained = False
        super().__init__(name, age, weight)
    def train(self):
        Dog.bark(self)
        self.trained = True
    def play(*args):
        dogs_list = [rex.name, torres.name,jimmy.name]
        dog_names = f', '.join(dogs_list)
        print(f'{dog_names} are playing together')
    def do_a_trick(self):
        if self.trained == True:
            if random.randint(0,100) < 25:
                print(f'{self.name} does a barrel roll')
            elif random.randint(0,100) < 50:
                print(f'{self.name} stands on his back legs')
            elif random.randint(0,100) < 75:
                print(f'{self.name} shakes your hand')
            elif random.randint(0,100) < 100:
                print(f'{self.name} plays dead')
        else:
            print('Your dog is not trained')


            

rex = PetDog('Rex', 7, 15, False)
torres = PetDog('Torres', 5, 18, False)
jimmy = PetDog('Jimmy', 9, 15, False)

#Testing that everything works
PetDog.train(torres)
PetDog.play()
PetDog.do_a_trick(rex)
        

        