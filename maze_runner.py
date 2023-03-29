def maze_runner(maze, directions):
    moves = {'N': [-1,0], 'S': [1,0], 'W': [0,-1], 'E': [0,1]}
    
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                current_point = [i, j]

    for step in directions:
        step_points = moves.get(step)
        current_point[0] += step_points[0]
        current_point[1] += step_points[1]
        if current_point[0] >= len(maze) or current_point[1] >= len(maze):
            return 'Dead'
        elif maze[current_point[0]][current_point[1]] == 1:
            return 'Dead'
        elif maze[current_point[0]][current_point[1]] == 3:
            return 'Finish'
        
    return 'Lost'

maze = [[0, 0, 0, 0, 3], [1, 0, 1, 1, 1], [0, 0, 2, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
directions = ['N', 'S', 'W', 'N', 'W', 'N', 'S', 'S', 'W', 'N', 'E', 'E', 'N', 'E', 'W', 'N', 'S', 'W', 'S']

print(maze_runner(maze, directions))