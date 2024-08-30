def printSpiral(size):
    
    row, col = 0, 0
 
    boundary = size - 1
    sizeLeft = size - 1
    flag = 1
 
    move = 'r'
 
    matrix = [[0 for j in range(size)] for i in range(size)]
 
    for i in range(1, size * size + 1):
        matrix[row][col] = i
 
        if move == 'r':
            col += 1
        elif move == 'l':
            col -= 1
        elif move == 'u':
            row -= 1
        elif move == 'd':
            row += 1
 
        if i == boundary:
            boundary += sizeLeft
 
            if flag != 2:
                flag = 2
            else:
                flag = 1
                sizeLeft -= 1
 
            # switch-case to rotate the movement
            if move == 'r':
                move = 'd'
            elif move == 'd':
                move = 'l'
            elif move == 'l':
                move = 'u'
            elif move == 'u':
                move = 'r'
 
    for row in range(size):
        for col in range(size):
            n = matrix[row][col]
            print(n, end='  ' if n < 10 else ' ')
        print()
 
size = 5
 
printSpiral(size)