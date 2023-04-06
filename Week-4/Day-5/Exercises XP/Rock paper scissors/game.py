import string
import random
valid_items = ['rock', 'paper', 'scissors']
num_games = 0
game_score = {'won': 0, 'lost': 0, 'draws': 0}
class Game:
    def __init__(self):
        pass
    def get_user_item(self):
        user_item = input('Select rock, paper or scissors ')
        if not user_item in valid_items:
            print('Choose a valid item!')
            Game.get_user_item(self)
        else:
            return user_item
    def get_computer_item(self):
        computer_item = random.choice(valid_items)
        return computer_item
    def get_game_result(self,user_item,computer_item):
        if user_item == computer_item:
            game_score['draws'] += 1
            return 'draw'
        elif (user_item == 'scissors' and computer_item == 'paper') or (user_item == 'rock' and computer_item == 'scissors') or (user_item == 'paper' and computer_item == 'rock'):
            game_score['won'] += 1
            return 'win'
        else:
            game_score['lost'] += 1
            return 'loss'
    def play(self):
        user_choice = Game.get_user_item(self)
        comp_choice = Game.get_computer_item(self)
        result = Game.get_game_result(self, user_choice, comp_choice)
        print(f'The result of a game: {result}! You chose {user_choice} and computer chose {comp_choice}')