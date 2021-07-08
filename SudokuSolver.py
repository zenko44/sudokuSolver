from array import *


# Sudoku rules:
#1. only the number 1 through 9 can be used

#2. the board is 9x9 and can be further seperated 
# into 3x3 areas

#3. in the 3x3 are the can be 0 duplicate numbers,
# this rule also applies to rows and columns on the 
# board as a whole
sudoku_array = ([[0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],          ## Front face of the sudoku cube
                [0, 0, 0,  0, 0, 0,  0, 0, 0],          ## [0][0 - 8][0 - 8]

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0]],

                [[0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],          # Top face of sudoku cube
                [0, 0, 0,  0, 0, 0,  0, 0, 0],          # [1][0 - 8][0 - 8]

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0]],

                [[0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # Bottom Face of sudoku cube
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # [2][0 - 8][0 - 8]

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0]],

                [[0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # Left face of Sudoku Cube
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # [3][0 - 8][0 - 8]

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0]],

                [[0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # Right face of sudoku Cube
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # [4][0 - 8][0 - 8]

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0]],

                [[0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # Back face of sudoku cube
                [0, 0, 0,  0, 0, 0,  0, 0, 0],  # [5][0 - 8][0 - 8]

                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0],
                [0, 0, 0,  0, 0, 0,  0, 0, 0]])



def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("+ + + + + + + + + + + + + ")

        for x in range(len(board[0])):
            if x % 3 == 0 and x != 0:
                print(" | ", end="")

            if x == 8:
                print(board[i][x])
            else:
                print(str(board[i][x]) + " ", end="")


def find_empty(board):
    for z in range(len(board)):
        for i in range(len(board[0])):
            for x in range(len(board[1])):
                if board[z][i][x] == 0:
                    return (z, i, x)  # row, col

    return None

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        face, row, col = find

    for i in range(1, 10):
        if valid(board, i, (face, row, col)):
            board[face][row][col] = i

            if solve(board):
                return True

            board[face][row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False


    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    box_z = pos[2] // 3

    for z in range(box_z * 3, box_z * 3 + 3):
        for i in range(box_y * 3, box_y * 3 + 3):
            for x in range(box_x * 3, box_x * 3 + 3):
                if board[i][x] == num and (i, x) != pos:
                    return False

    return True


def print_board(board):
    for z in range(len(board)):
        if z % 3 == 0 and z != 0:
            print("......................")
        for i in range(len(board[0])):
            if i % 3 == 0 and i != 0:
                print("---------------------------")

            for x in range(len(board[1])):
                if x % 3 == 0 and x != 0:
                    print(" | ", end="")

                if x == 8:
                    print(board[z][i][x])
                else:
                    print(str(board[z][i][x]) + " ", end="")
                   


def find_empty(board):
    for z in range(len(board)):
        for i in range(len(board[0])):
            for x in range(len(board[1])):
                if board[z][i][x] == 0:
                    return (z, i, x)  # row, col

    return None


print_board(sudoku_array)
solve(sudoku_array)
print("___________________")
print_board(sudoku_array)
