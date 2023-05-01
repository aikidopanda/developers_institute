import os
import django
import sys
import random
import math

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homm_cardgame.settings')
django.setup()

from game.models import *

player_deck, opponent_deck, player_hand, opponent_hand, player_discard, opponent_discard = [], [], [], [], [], []

player_board = {
    'front': [None, None, None, None],
    'rear': [None, None, None, None],
}

opponent_board = {
    'front': [None, None, None, None],
    'rear': [None, None, None, None],
}

turn_num = 0

coinflip = random.randint(1, 2)

if coinflip == 1:
    player_first = True
else:
    player_first = False

human_player = Player.objects.get(human=True)
opponent_player = Player.objects.get(human=False)


def start_game():
    player_name = input('Enter the player name!')
    human_player = Player(name=player_name, health=20, games_won=0, gold=0, human=True)
    computer_player = Player(name='Opponent', health=20, games_won=0, gold=0, human=False)
    human_player.save()
    computer_player.save()
    create_factions()
    create_units_deck(player_deck)
    create_units_deck(opponent_deck)
    # Dealing 3 starting cards
    for i in range(2):
        deal_card(player_deck, player_hand)
        deal_card(opponent_deck, opponent_hand)
    turn()
    # here should be building of the deck and the board


def main_menu():
    user_choice = input(
        'S - start a new game, Q - quit, C - clean the database(admin)')
    if user_choice.upper() == 'S':
        start_game()
    elif user_choice.upper() == 'Q':
        print('See you next time!')
        sys.exit()
    elif user_choice.upper() == 'C':
        cleanup()
        main_menu()
    else:
        print('Invalid input! Press either S to start a game or Q for exit')
        main_menu()


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
            faction=Faction.objects.get(name='Castle')
        )
        deck.append(pikeman)
        pikeman.save()

    for i in range(6):
        archer = Card(
            name='Archer',
            health=2,
            health_base=2,
            attack=2,
            cost=3,
            ranged=True,
            flying=False,
            faction=Faction.objects.get(name='Castle')
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
            faction=Faction.objects.get(name='Castle')
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
            faction=Faction.objects.get(name='Castle')
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
            faction=Faction.objects.get(name='Castle')
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
            faction=Faction.objects.get(name='Castle')
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
        faction=Faction.objects.get(name='Castle')
    )
    deck.append(angel)
    angel.save()

    random.shuffle(deck)

    # return shuffled


def deal_card(deck, hand):
    if len(deck) > 0:
        card = deck.pop()
        hand.append(card)


def player_turn():
    passed = False

    # global human_player
    human_player = Player.objects.get(human=True)
    opponent_player = Player.objects.get(human=False)
    turn_income = 2 + math.floor(turn_num/3)
    human_player.gold += turn_income
    if human_player.gold > turn_income * 2:
        human_player.gold = turn_income * 2
    human_player.save()
    if len(player_deck) > 0:
        deal_card(player_deck, player_hand)
    if player_first == True:
        action = 'attacking'
    else:
        action = 'defending'

    while passed == False:

        print(f'Its turn {turn_num}. You are {action} this turn. Your cards are: {player_hand}. You have {human_player.gold} gold\n You have {human_player.health} health and your opponent has {opponent_player.health}\n')
        # player chooses a card to play
        c = input(
            'Choose a card to play (enter a card number, from left to right) or press P to pass: ')
        if c.upper() == 'P':
            passed = True
            break
        else:
            intc = int(c)
        card = player_hand[intc - 1]
        if card.cost > human_player.gold:
            print('Not enough gold, choose another card or pass')
            continue
        # player chooses a field on the board where to play the card
        f = input(f'You chose {card}. Choose a place on the board where to play your card, separated by a comma. For example: front, 2 for second position on the frontline: ')
        splitted = f.split(',')
        row = splitted[0]
        col = int(splitted[1])

        if player_board[row][col - 1] != None:
            print('This field is already occupied')
        else:
            player_board[row][col - 1] = card
            player_hand.remove(card)
            human_player.gold = human_player.gold - card.cost
            human_player.save()
        display_board()


def opponent_turn():
    opponent_player = Player.objects.get(human=False)
    turn_income_ai = 3 + math.floor(turn_num/3)
    opponent_player.gold += turn_income_ai
    if opponent_player.gold > turn_income_ai * 2:# The limit for gold, motivating players to spend it and play cards
        opponent_player.gold = turn_income_ai * 2
    opponent_player.save()

    if len(opponent_deck) > 0:
        deal_card(opponent_deck, opponent_hand)

    while opponent_player.gold > 0:
        hand_to_play = []
        card_placed = False
        random_placer = random.randint(1, 10)
        for i in range(len(opponent_hand)):
            if opponent_hand[i].cost <= opponent_player.gold:
                hand_to_play.append(opponent_hand[i])
        if len(hand_to_play) == 0:
            break
        else:
            c = random.choice(hand_to_play)
        print(opponent_player.gold)
        if c.ranged == False:
            for k, v in opponent_board.items():
                for i in range(len(v)):
                    if v[i] == None and card_placed == False and random_placer >= 6:
                        v[i] = c
                        card_placed = True
                        opponent_player.gold = opponent_player.gold - c.cost
                        opponent_player.save()
                    else:
                        random_placer += 2
        else:
            for k, v in opponent_board.items():
                for i in range(len(v)):
                    if k != 'front' and random_placer >= 6:
                        if v[i] == None and card_placed == False:
                            v[i] = c
                            card_placed = True
                            opponent_player.gold = opponent_player.gold - c.cost
                            opponent_player.save()
                        else:
                            random_placer += 2

        hand_to_play = []
        opponent_hand.remove(c)


def attacking(line):
    global player_discard, opponent_discard

    human_player = Player.objects.get(human=True)
    opponent_player = Player.objects.get(human=False)

    if player_first == True:
        enemyfront = opponent_board['front']
        enemyrear = opponent_board['rear']
        enemy = opponent_player
    else:
        enemyfront = player_board['front']
        enemyrear = player_board['rear']
        enemy = human_player

    discard1, discard2 = [], [] # discard1 is the attacking side discard, discard2 is the defending start discard

    for i in range(len(line)):
        if line[i] != None:
            if enemyfront[i] != None:
                if line[i].ranged == False:
                    line[i].fight_melee(enemyfront[i])
                else:
                    line[i].fight_range(enemyfront[i])
                if enemyfront[i].health <= 0:
                    discard2.append(enemyfront[i])
                    enemyfront[i] = None
                if line[i].health <= 0:
                    discard1.append(line[i])
                    line[i] = None
            elif enemyrear[i] != None:
                if line[i].ranged == False:
                    line[i].fight_melee(enemyrear[i])
                else:
                    line[i].fight_range(enemyrear[i])
                if enemyrear[i].health <= 0:
                    discard2.append(enemyrear[i])
                    enemyrear[i] = None
                if line[i].health <= 0:
                    discard1.append(line[i])
                    line[i] = None
            else:
                line[i].fight_melee(enemy)
                enemy.save()

    if player_first == True:
        player_discard += discard1
        opponent_discard += discard2
    else:
        player_discard += discard2
        opponent_discard += discard1


def turn():
    global turn_num
    human_player = Player.objects.get(human=True)
    opponent_player = Player.objects.get(human=False)
    player_turn()
    opponent_turn()
    # Units attacking each other
    if player_first == True:
        for line in ['front', 'rear']:
            attacking(player_board[line])
    else:
        for line in ['front', 'rear']:
            attacking(opponent_board[line])
    # Victory check
    if human_player.health <= 0:
        opponent_player.games_won += 1
        print(
            f'Defeat! The score is {human_player.games_won} : {opponent_player.games_won}')
        new_round()
    elif opponent_player.health <= 0:
        human_player.games_won += 1
        print(
            f'Victory! The score is {human_player.games_won} : {opponent_player.games_won}')
        new_round()
    else:
        turn_pass()


def new_round():
    global turn_num, player_hand, opponent_hand, player_board, opponent_board
    human_player = Player.objects.get(human=True)
    opponent_player = Player.objects.get(human=False)
    if human_player.games_won == 2:
        print('You won the match!')
        main_menu()
    elif opponent_player.games_won == 2:
        print('You lost the match! Returning into main menu')
        main_menu()
    player_hand, opponent_hand = [], []
    player_board = {
        'front': [None, None, None, None],
        'rear': [None, None, None],
    }
    opponent_board = {
        'front': [None, None, None, None],
        'rear': [None, None, None, None],
    }
    human_player.health, human_player.gold = 20, 0
    opponent_player.health, opponent_player.gold = 20, 0
    turn_num = 0
    for i in range(2):
        deal_card(player_deck, player_hand)
        deal_card(opponent_deck, opponent_hand)
    turn()


def turn_pass():
    global player_first, turn_num
    if player_first == True:
        player_first = False
    else:
        player_first = True
    display_board()
    turn_num += 1
    turn()


def display_board():
    print(f"\n {opponent_board['rear']}\n {opponent_board['front']}\n\n {player_board['front']}\n {player_board['rear']}\n\n")


def cleanup():
    Card.objects.all().delete()
    Player.objects.all().delete()
    Faction.objects.all().delete()


main_menu()
