import game
import sys
def get_user_menu_choice():
    choice = input('G - start a new game, S - show scores, Q - quit')
    return choice.upper()
def print_results():
    print(f'Current results are: {game.game_score}. Thank you for playing. hope you enjoyed:)')
def main():
    userkey = get_user_menu_choice()
    if userkey == 'G':
        new_game = game.Game()
        new_game.play()
    elif userkey == 'S':
        print_results()
    elif userkey == 'Q':
        print_results()
        sys.exit()
    main()
main()

