from Anagram_checker import Anagram_checker
import sys
def menu_choice():
    user_choice = input('Press W to enter a new word to find its anagrams or press Q for exit ')
    return user_choice.upper()
def main():
    choice = menu_choice()
    if choice == 'W':
        user_word = input('Enter a word: ')
        if Anagram_checker.is_valid_word(user_word) == True:
            user_word = user_word.strip()
            new_checker = Anagram_checker()
            new_checker.get_anagrams(user_word)
            print(f'The anagrams for {user_word} are {new_checker.get_anagrams(user_word)}')
        else:
            print('You word is invalid. Enter another one')
    elif choice == 'Q':
        sys.exit()
    else:
        print('Invalid key/ Press either W to enter a word or Q to quit')
    main()
main()

    


