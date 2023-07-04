import os
import django
import random
import math

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homm_cardgame.settings')
django.setup()

from game.models import *

turn_num = 0

def create_factions():
    castle = Faction(name = 'Castle')
    castle.save()

def create_units_deck(deck):

    for i in range(7):
        pikeman = Card(
            name='Pikeman',
            health=4,
            health_base=4,
            attack=2,
            cost=2,
            ranged=False,
            flying=False,
            faction=Faction.objects.get(name='Castle'),
            image = 'game/images/Pikeman.webp'
        )
        deck.append(pikeman)
        pikeman.save()

    for i in range(6):
        archer = Card(
            name='Archer',
            health=2,
            health_base=2,
            attack=3,
            cost=3,
            ranged=True,
            flying=False,
            faction=Faction.objects.get(name='Castle'),
            image = 'game/images/Archer.webp'
        )
        deck.append(archer)
        archer.save()

    for i in range(5):
        griffin = Card(
            name='Royal Griffin',
            health=7,
            health_base=7,
            attack=4,
            cost=4,
            ranged=False,
            flying=True,
            faction=Faction.objects.get(name='Castle'),
            image = 'game/images/Royal Griffin.webp'
        )
        deck.append(griffin)
        griffin.save()

    for i in range(4):
        knight = Card(
            name='Knight',
            health=8,
            health_base=8,
            attack=5,
            cost=5,
            ranged=False,
            flying=False,
            faction=Faction.objects.get(name='Castle'),
            image = 'game/images/Knight.webp'
        )
        deck.append(knight)
        knight.save()

    for i in range(3):
        monk = Card(
            name='Monk',
            health=6,
            health_base=6,
            attack=3,
            cost=6,
            ranged=True,
            flying=False,
            faction=Faction.objects.get(name='Castle'),
            image = 'game/images/Monk.webp'
        )
        deck.append(monk)
        monk.save()

    for i in range(2):
        champion = Card(
            name='Champion',
            health=12,
            health_base=12,
            attack=7,
            cost=7,
            ranged=False,
            flying=False,
            faction=Faction.objects.get(name='Castle'),
            image = 'game/images/Champion.webp'
        )
        deck.append(champion)
        champion.save()

    angel = Card(
        name='Angel',
        health=15,
        health_base=15,
        attack=10,
        cost=8,
        ranged=False,
        flying=True,
        faction=Faction.objects.get(name='Castle'),
        image = 'game/images/Angel.webp'
    )
    deck.append(angel)
    angel.save()

    random.shuffle(deck)

def deal_card(deck, hand):
    if len(deck) > 0:
        card = deck.pop()
        hand.append(card)


def cleanup():
    Card.objects.all().delete()
    Faction.objects.all().delete()