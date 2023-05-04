import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homm_cardgame.settings')
django.setup()

from main_things import *
from game.models import *

longspear = ['Pikeman']

def attacked(attacker, target): #Units with long spear hit enemy before he attacks

    if target.name in longspear:
        attacker.health -= 1
        attacker.save()
        if attacker.health <= 0:
            attacker = None

