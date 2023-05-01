from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    games_won = models.IntegerField()
    gold = models.IntegerField()
    health = models.IntegerField()
    human = models.BooleanField()
    attack = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}, {self.health}, {self.gold}'



class Faction(models.Model):

    name = models.CharField(default='Neutral')

    def _str_(self):
        return f'{self.name}'


class Card(models.Model):
    name = models.CharField(max_length=30)
    health = models.IntegerField()
    health_base = models.IntegerField(default=0)
    attack = models.IntegerField()
    cost = models.IntegerField()
    ranged = models.BooleanField()
    flying = models.BooleanField()
    attacked_this_turn = models.BooleanField(default=False)
    image = models.CharField(max_length=100, default=f'images/placeholder.webp',null=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}, health: {self.health}, attack: {self.attack}, cost: {self.cost}'
    
    def fight_range(self, other):
        other.health = other.health - self.attack
        other.save()
        self.save()

    def fight_melee(self, other):
        other.health -= self.attack
        self.health -= other.attack
        other.save()
        self.save()





# Create your models here.
