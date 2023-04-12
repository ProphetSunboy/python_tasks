def street_fighter_selection(fighters, initial_position, moves):
    position = list(initial_position)
    moves_dict = {'up': [0,1], 'down': [0,-1], 'left': [-1,0], 'right': [1,0]}
    solution = []
    
    for move in moves:
        position[0] += moves_dict[move][0]
        
        if position[0] > 5:
            position[0] = 0
        elif position[0] < 0:
            position[0] = 5
            
        if position[1] + moves_dict[move][1] in [0, 1]:
            position[1] += moves_dict[move][1]
        
        solution.append(fighters[position[0]][position[1]])
        
    return solution

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
moves =  ["left"]*8
solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
print(street_fighter_selection(fighters,(0,0), moves))