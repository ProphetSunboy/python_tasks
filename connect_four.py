def who_is_winner(pieces_position_list):
    '''
    This function creates a connect four game board and returns the results
    of the game. 
    Input parameters: list of the sequence of moves in a game
    of the "Field_Player" format
    '''
    # Creating game field
    grids = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    players = {'Yellow': 0, 'Red': 1}
    field = []
    [field.append([]) for _ in range(7)]

    res = ''
    for i,piece in enumerate(pieces_position_list):
        move, player = piece.split('_')
        field[grids[move]].append(players[player])
        res = checker(field)
        if res:
            return res
    return 'Draw'

def checker(field):
    '''
    Subfunction of the who_is_winner function, returns the name of the winner,
    if any, or None
    Input parameters: game board
    '''
    # Check if a player wins by columns  
    for i in range(len(field)):
        for j in range(len(field[i])):
            if len(field[i][j:j+4]) == 4:
                if all(field[i][j:j+4]):
                    return 'Red'
                elif all([0 == point for point in field[i][j:j+4]]):
                    return 'Yellow'

    # Check if a player wins by rows            
    for i in range(6):
        for j in range(len(field)):
            if len(field[j:j+4]) == 4:
                if all(len(col) > i if len(col) > 0 else False for col in field[j:j+4]):
                    if all(col[i] for col in field[j:j+4]):
                        return 'Red'
                    elif all(col[i] == 0 for col in field[j:j+4]):
                        return 'Yellow'
    
    for i in range(len(field)-3):
        for j in range(len(field[i])):
            if len(field[i]) >= j:
                # Check if the player wins diagonally to the right up
                if (j+2<=len(field[i+1])<=6) and (j+3<=len(field[i+2])<=6) and (j+4<=len(field[i+3])<=6):
                    if field[i][j] == 1 and field[i+1][j+1] == 1 and field[i+2][j+2] == 1 and field[i+3][j+3] == 1:
                        return 'Red'
                    elif field[i][j] == 0 and field[i+1][j+1] == 0 and field[i+2][j+2] == 0 and field[i+3][j+3] == 0:
                        return 'Yellow'

                # Check if the player wins diagonally to the right down    
                if (0<j<=len(field[i+1])) and (0<j-1<=len(field[i+2])) and (0<j-2<=len(field[i+3])):
                    if field[i][j] == 1 and field[i+1][j-1] == 1 and field[i+2][j-2] == 1 and field[i+3][j-3] == 1:
                        return 'Red'
                    elif field[i][j] == 0 and field[i+1][j-1] == 0 and field[i+2][j-2] == 0 and field[i+3][j-3] == 0:
                        return 'Yellow'

# Few tests
pieces_position_list = [
    ["C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"],
    ["A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"],
    ["F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", 
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", 
"B_Yellow", "B_Red"],
]

for position in pieces_position_list:
    print(who_is_winner(position))