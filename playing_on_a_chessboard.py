import numpy

def game(n):
    board = []
    for i in range(n):
        counter = i+1
        board.append([])
        for j in range(1, n+1):
            counter += 1
            board[i].append(j/counter)

    for row in board:
        print(row)

    x = numpy.array([numpy.array(i) for i in board])
    return x.sum()

print(game(1))