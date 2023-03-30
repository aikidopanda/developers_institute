player = 1
mark = 'X'
turns = 1
winner = False
newgame = ''

game_data = {
    'top':[' ', ' ', ' '],
    'center':[' ', ' ', ' '],
    'bottom':[' ', ' ', ' ']
}

def start_game():
    player = 1
    mark = 'X'
    turns = 1
    winner = False

    for key in game_data:
        game_data[key] = [' ', ' ', ' ']

    display()
    player_input()


#expected input values, to prevent players from giving any words except rows and columns
valid_rows = ['top','center','bottom']
valid_cols = [0,1,2]

def turn_order(playernum):
    global player
    global mark
    global turns
    global winner
    global newgame
    print(turns)
    display()
    for key in game_data: # horizontal win
        if game_data[key] == ['X', 'X', 'X'] or game_data[key] == ['O', 'O', 'O']:
            newgame = input(f'Player {player} has won! Wanna play a new game? (Y/N) ')
    i = 0
    while i < 3: #vertical win       
        if set([game_data['top'][i], game_data['center'][i], game_data['bottom'][i]]) == {'X'} or set([game_data['top'][i], game_data['center'][i], game_data['bottom'][i]]) == {'O'}:
            newgame = input(f'Player {player} has won! Wanna play a new game? (Y/N) ')
            winner = True
        i += 1
        # diagonal win
    if set([game_data['top'][0], game_data['center'][1], game_data['bottom'][2]]) == {'X'} or set([game_data['top'][0], game_data['center'][1], game_data['bottom'][2]]) == {'O'}:
        newgame = input(f'Player {player} has won! Wanna play a new game? (Y/N) ')
        winner = True
    if set([game_data['top'][2], game_data['center'][1], game_data['bottom'][0]]) == {'X'} or set([game_data['top'][2], game_data['center'][1], game_data['bottom'][0]]) == {'O'}:
        newgame = input(f'Player {player} has won! Wanna play a new game? (Y/N) ')
        winner = True
    if turns >= 9 and winner == False:
        newgame = input('A draw! Wanna play a new game? (Y/N) ')
    #turn pass
    if playernum == 1:
        player = 2
        mark = 'O'
    else:
        player = 1
        mark = 'X'
    #starting a new game, if the current one was finished
    if newgame == 'Y':
        start_game()
    elif newgame == 'N':
        print('Ok! Hope you enjoyed playing')


def display():
    row1, row2, row3, row4, row5 = '','','','',''
    i = 0
    while i <= 13: #top and bottom borders, not changing
        if i == 13:
            row1 += '\n'
        else:
            row1 += '*'
        i += 1
    i = 0

    while i <= 13:
        if i == 2:
            row2 += game_data['top'][0]
        elif i == 6:
            row2 += game_data['top'][1]
        elif i == 10:
            row2 += game_data['top'][2]
        elif i == 0 or i == 12:
            row2 += '*'
        elif i == 4 or i == 8:
            row2 += '|'
        elif i == 13:
            row2 += '\n'
        else:
            row2 += ' '
        i += 1
    i = 0

    while i <= 13:
        if i == 2:
            row3 += game_data['center'][0]
        elif i == 6:
            row3 += game_data['center'][1]
        elif i == 10:
            row3 += game_data['center'][2]
        elif i == 0 or i == 12:
            row3 += '*'
        elif i == 4 or i == 8:
            row3 += '|'
        elif i == 13:
            row3 += '\n'
        else:
            row3 += ' '
        i += 1
    i = 0

    while i <= 13:
        if i == 2:
            row4 += game_data['bottom'][0]
        elif i == 6:
            row4 += game_data['bottom'][1]
        elif i == 10:
            row4 += game_data['bottom'][2]
        elif i == 0 or i == 12:
            row4 += '*'
        elif i == 4 or i == 8:
            row4 += '|'
        elif i == 13:
            row4 += '\n'
        else:
            row4 += ' '
        i += 1
    i = 0

    while i <= 13: #border between rows, not changing
        if i == 0 or i == 12:
            row5 += '*'
        elif i == 4 or i == 8:
            row5 += '|'
        elif i == 13:
            row5 += '\n'
        else:
            row5 += '-'
        i += 1
    i = 0 
    grid = ''
    j = 0
    while j < 7:
        if j == 0 or j == 6:
            grid += row1
        elif j == 1:
            grid += row2
        elif j == 3:
            grid += row3 
        elif j == 5:
            grid += row4  
        else:
            grid += row5
        j += 1

    print(grid)

def turn(row,col):
    global turns
    if game_data[row][col] != ' ':
        print ('This square already contains X or O. Choose another square!')
    elif not row in valid_rows or not col in valid_cols:
        print('You entered invalid row or column. Read the instruction!')
    else:
        if row == 'top':
            if col == 0:
                game_data['top'][0] = mark
            elif col == 1:
                game_data['top'][1] = mark
            elif col == 2:
                game_data['top'][2] = mark
        elif row == 'center':
            if col == 0:
                game_data['center'][0] = mark
            elif col== 1:
                game_data['center'][1] = mark
            elif col == 2:
                game_data['center'][2] = mark
        elif row == 'bottom':
            if col == 0:
                game_data['bottom'][0] = mark
            elif col == 1:
                game_data['bottom'][1] = mark
            elif col == 2:
                game_data['bottom'][2] = mark
        turn_order(player)
        turns += 1
    if winner == False and turns <= 9:
        player_input()

def player_input():
    user_input = input('Enter a row and a column, separated by space in the following format: top/center/bottom left/center/right ')
    list_temp = user_input.split()
    user_row, user_col = list_temp[0],list_temp[1]
    if user_col == 'left':
        user_col = 0
    elif user_col == 'center':
        user_col = 1
    elif user_col == 'right':
        user_col = 2
    else:
        print('Enter a valid name of row/column!')
    turn(user_row,user_col)

start_game()



