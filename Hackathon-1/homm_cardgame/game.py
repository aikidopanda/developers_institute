from main_things import *
from game.models import *
import os
import django
import pygame
from pygame.locals import *

#card size: width 87 height 115. Pin it here since it will be standard for all cards

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homm_cardgame.settings')
django.setup()


pygame.init()

CLOCK = pygame.time.Clock()
FPS = 30

clicked = False
initialized = False

#Colours of the buttons and badges
black = (0, 0, 0)
blue = (88, 60, 178)
red = (204, 0, 0)
yellow = (244, 250, 47)
white = (255, 255, 255)
maroon = (128, 0, 0)

player_color = (48, 19, 196)
opponent_color = (192, 42, 19)

active_card = None

coinflip = random.randint(1, 2)
if coinflip == 1:
    player_first = True
else:
    player_first = False


bg = pygame.image.load('game/images/background.jpg')
font = pygame.font.SysFont('Arial', 20)

screen = pygame.display.set_mode((1600, 900), pygame.SCALED)
pygame.display.set_caption('Heroes of Might and Magic card game')

menurunning = True
gamerunning = False

# GUI drawing functions

def text_objects(text, font):
    textSurface = font.render(text, True, maroon)
    return textSurface, textSurface.get_rect()


def text_objects_sm(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, width, height, colour, status, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if status == 'active':
            colour = maroon
        if click[0] == 1 and action != None and clicked == False:
            action()

    pygame.draw.rect(screen, colour, (x, y, width, height))

    smallText = pygame.font.Font("freesansbold.ttf", 18)
    textSurf, textRect = text_objects_sm(msg, smallText)
    textRect.center = ((x+(width/2)), (y+(height/2)))
    screen.blit(textSurf, textRect)


def button_round(msg, x, y, radius, colour, status, action=None):
    global clicked
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + radius > mouse[0] > x - radius and y + radius > mouse[1] > y - radius:
        if status == 'active':
            colour = maroon
        if click[0] == 1 and action != None and clicked == False:
            clicked = True
            action()

    pygame.draw.circle(screen, colour, (x, y), radius)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects_sm(msg, smallText)
    textRect.center = ((x), (y))
    screen.blit(textSurf, textRect)


def cardtoplay(x, y, width, height, index):
    global active_card
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    screen.blit(pygame.image.load(
            player_hand[index].image), (x, y))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and human_player.gold >= player_hand[index].cost:
            human_player.gold = human_player.gold - player_hand[index].cost
            active_card = player_hand.pop(index)
            human_player.save()


def cardslot(x, y, width, height, colour, index):
    global active_card
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1:
            player_board['front'][index] = active_card
            active_card = None
    if player_board['front'][index] != None:
        screen.blit(pygame.image.load(
            player_board['front'][index].image), (x, y))
    else:
        pygame.draw.rect(screen, colour, (x, y, width, height))


def cardslot_rear(x, y, width, height, colour, index):
    global active_card
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1:
            player_board['rear'][index] = active_card
            active_card = None
    if player_board['rear'][index] != None:
        screen.blit(pygame.image.load(
            player_board['rear'][index].image), (x, y))
    else:
        pygame.draw.rect(screen, colour, (x, y, width, height))


def cardslot_opponent(x, y, width, height, colour, index):
    if opponent_board['front'][index] != None:
        screen.blit(pygame.image.load(
            opponent_board['front'][index].image), (x, y))
    else:
        pygame.draw.rect(screen, colour, (x, y, width, height))


def cardslot_opponent_rear(x, y, width, height, colour, index):
    if opponent_board['rear'][index] != None:
        screen.blit(pygame.image.load(
            opponent_board['rear'][index].image), (x, y))
    else:
        pygame.draw.rect(screen, colour, (x, y, width, height))


# Gameplay functions
def start():
    global menurunning, gamerunning
    menurunning = False
    gamerunning = True
    start_game()
    player_turn_gui()

def menuexit():
    global menurunning, gamerunning
    gamerunning = False
    menurunning = True #doesn't work as intended yet, should work on it when I have time

def exit_game():
    global menurunning
    global gamerunning
    menurunning = False
    gamerunning = False


def processing():
    global turn_num, clicked
    opponent_turn()
    pygame.time.delay(1500)
    if player_first == True:
        for line in ['rear', 'front']:
            attacking(player_board[line])
    else:
        for line in ['rear', 'front']:
            attacking(opponent_board[line])
    for v in player_board.values():
        for i in range(len(v)):
            if v[i] != None:
                v[i].endofturn(player_board)
    for v in opponent_board.values():
        for i in range(len(v)):
            if v[i] != None:
                v[i].endofturn(opponent_board)
    pygame.time.delay(1000)
    clicked = False
    turn_num += 1
    player_turn_gui()


def player_turn_gui():

    global turn_num, clicked, player_first

    if player_first == True:
        player_first = False
    else:
        player_first = True

    human_player = Player.objects.get(human=True)
    turn_income = 2 + math.floor(turn_num/3)
    human_player.gold += turn_income
    if human_player.gold > turn_income * 2:
        human_player.gold = turn_income * 2 # The max amount of gold players can keep should be limited, otherwise cards will be hoarded to build a decisive combo
    human_player.save()
    if len(player_deck) > 0:
        deal_card(player_deck, player_hand)


def opponent_turn():
    opponent_player = Player.objects.get(human=False)
    turn_income_ai = 2 + math.floor(turn_num/2) # computer opponent gets more gold than player, otherwise it's too easy to beat
    opponent_player.gold += turn_income_ai
    if opponent_player.gold > turn_income_ai * 2:
        opponent_player.gold = turn_income_ai * 2
    opponent_player.save()

    if len(opponent_deck) > 0:
        deal_card(opponent_deck, opponent_hand)

    while opponent_player.gold > 0:
        hand_to_play = []
        card_placed = False
        random_placer = random.randint(1, 10) # Not the best strategy, but at least opponent won't be 100% predictable:)
        for i in range(len(opponent_hand)):
            if opponent_hand[i].cost <= opponent_player.gold:
                hand_to_play.append(opponent_hand[i]) # Choosing from computer player's hand all the cards he is actually able to play
        if len(hand_to_play) == 0:
            break
        else:
            index = random.randint(0, len(hand_to_play) - 1)
            c = hand_to_play.pop(index) # Computer opponent chooses a card
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
                    if k == 'rear' and random_placer >= 6:
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
    global player_discard, opponent_discard # Not used yet, but it's surely necessary for my future plans

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

    # discard1 is attacker discard, discard2 is defender discard
    discard1, discard2 = [], []

    for i in range(len(line)):
        if line[i] != None:
            if enemyfront[i] != None:
                if line[i].ranged == False:
                    line[i].fight_melee(enemyfront[i])
                else:
                    line[i].fight_range(enemyfront[i])
                if enemyfront[i].health <= 0:
                    discard2.append(enemyfront[i])
                    enemyfront[i] = None # If card is killed, clear its slot
            elif enemyrear[i] != None:
                if line[i].ranged == False:
                    line[i].fight_melee(enemyrear[i])
                else:
                    line[i].fight_range(enemyrear[i])
                if enemyrear[i].health <= 0:
                    discard2.append(enemyrear[i])
                    enemyrear[i] = None
            else:
                line[i].fight_melee(enemy)
                enemy.save()
            if line[i] and line[i].health <= 0:
                discard1.append(line[i])
                line[i] = None

    if player_first == True:
        player_discard += discard1
        opponent_discard += discard2
    else:
        player_discard += discard2
        opponent_discard += discard1

def cancel_card():
    global active_card
    human_player = Player.objects.get(human=True)
    if active_card != None:
        human_player.gold += active_card.cost
        player_hand.append(active_card)
        active_card = None
        human_player.save()



# Main menu
while menurunning:
    screen.blit(bg, (0, 0))

    if initialized == False:
        cleanup()
        initialized = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menurunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menurunning = False

    largeText = pygame.font.Font('freesansbold.ttf', 95)
    TextSurf, TextRect = text_objects("HoMM Card game", largeText)
    TextRect.center = (800, 300)
    screen.blit(TextSurf, TextRect)

    button('Start game', 700, 500, 200, 100, red, 'active', start)
    button('Quit', 700, 650, 200, 100, red, 'active', exit_game)

    pygame.display.flip()
    CLOCK.tick(FPS)

# Game window
while gamerunning:
    screen.blit(bg, (0, 0))

    human_player = Player.objects.get(human=True)
    opponent_player = Player.objects.get(human=False)

    if player_first == True:
        action = 'attacking'
    else:
        action = 'defending'

    if human_player.health <= 0:
        status = 'Defeat!'
    elif opponent_player.health <= 0:
        status = 'Victory!'
    elif human_player.health <= 0 and opponent_player.health <= 0:
        status = 'Tie!'

    largeText = pygame.font.Font('freesansbold.ttf', 40)

    button("Active card",
           10, 10, 150, 50, player_color, 'passive')
    if active_card != None:
        screen.blit(pygame.image.load(
            active_card.image), (51.5,60))
    button("Change",
           10, 175, 150, 50, player_color, 'active', cancel_card)

    if human_player.health <= 0 or opponent_player.health <= 0:
        button(f"{status} Press Esc to quit",
                          10, 825, 800, 80, player_color,'passive')
    else:
        button(f"Its turn {turn_num}. You are {action}. Press the card or its number on keyboard to play it",
                          10, 825, 800, 80, player_color,'passive')

    for j in range(2):
        if j == 0:
            for i in range(4):
                cardslot(873 + i * 100, 525 + j * 150,
                         87, 115, player_color, i)
                if player_board['front'][i]:
                    button(f"{player_board['front'][i].attack} | {player_board['front'][i].health}",
                          873 + i * 100, 640 + j * 150, 87, 20, player_color, 'passive')
        if j == 1:
            for i in range(4):
                cardslot_rear(873 + i * 100, 525 + j * 150,
                              87, 115, player_color, i)
                if player_board['rear'][i]:
                    button(f"{player_board['rear'][i].attack} | {player_board['rear'][i].health}",
                          873 + i * 100, 640 + j * 150, 87, 20, player_color, 'passive')

    for j in range(2):
        if j == 0:
            for i in range(4):
                cardslot_opponent_rear(
                    873 + i * 100, 25 + j * 150, 87, 115, opponent_color, i)
                if opponent_board['rear'][i]:
                    button(f"{opponent_board['rear'][i].attack} | {opponent_board['rear'][i].health}",
                          873 + i * 100, 140 + j * 150, 87, 20, opponent_color, 'passive')
        if j == 1:
            for i in range(4):
                cardslot_opponent(873 + i * 100, 25 + j * 150,
                                  87, 115, opponent_color, i)
                if opponent_board['front'][i]:
                    button(f"{opponent_board['front'][i].attack} | {opponent_board['front'][i].health}",
                          873 + i * 100, 140 + j * 150, 87, 20, opponent_color, 'passive')

    for i, card in enumerate(player_hand):
        cardtoplay(20 + i * 100, 710, 87, 115, i)
        # screen.blit(pygame.image.load(
        #     player_hand[i].image), (20 + i * 100, 710))
        button(f"{i + 1}",
                        43 + i * 100, 640, 43, 20, player_color, 'passive')
        button(f"{card.attack} | {card.health}",
                        20 + i * 100, 690, 87, 20, opponent_color, 'passive')
        button(f"Cost: {card.cost}",
                        20 + i * 100, 660, 87, 20, maroon, 'passive')

    button_round(f'End turn (Space)', 1060, 410, 95, red, 'active', processing)

    button_round(f'{human_player.health} HP', 1375, 660, 50, maroon, 'passive')
    button_round(f'{opponent_player.health} HP', 1375, 170, 50, maroon, 'passive')
    button_round(f'{human_player.gold} Gold', 1475, 660, 50, maroon, 'passive')
    button_round(f'{opponent_player.gold} Gold', 1475, 170, 50, maroon, 'passive')

    for event in pygame.event.get():
        human_player = Player.objects.get(human=True)
        opponent_player = Player.objects.get(human=False)
        if event.type == pygame.QUIT:
            gamerunning = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menuexit()

            if event.key == K_1 and player_hand[0] != None and human_player.gold >= player_hand[0].cost:
                human_player.gold = human_player.gold - player_hand[0].cost
                active_card = player_hand.pop(0)
            elif event.key == K_2 and player_hand[1] != None and human_player.gold >= player_hand[1].cost:
                human_player.gold = human_player.gold - player_hand[1].cost
                active_card = player_hand.pop(1)
            elif event.key == K_3 and player_hand[2] != None and human_player.gold >= player_hand[2].cost:
                human_player.gold = human_player.gold - player_hand[2].cost
                active_card = player_hand.pop(2)
            elif event.key == K_4 and player_hand[3] != None and human_player.gold >= player_hand[3].cost:
                human_player.gold = human_player.gold - player_hand[3].cost
                active_card = player_hand.pop(3)
            elif event.key == K_5 and player_hand[4] != None and human_player.gold >= player_hand[4].cost:
                human_player.gold = human_player.gold - player_hand[4].cost
                active_card = player_hand.pop(4)
            elif event.key == K_6 and player_hand[5] != None and human_player.gold >= player_hand[5].cost:
                human_player.gold = human_player.gold - player_hand[5].cost
                active_card = player_hand.pop(5)
            human_player.save()

            if event.key == K_SPACE:
                processing()

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
