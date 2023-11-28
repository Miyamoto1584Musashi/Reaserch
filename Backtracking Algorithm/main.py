
def writing_sudoku(board):
    """Sudoku output to the screen"""

    for i in range(0, len(board)):
        if i % 3 == 0:
            print('- - - - - - - - - - - - -')
        for j in range(0, len(board)):
            if j % 3 == 0:
                print('|', end=' ')
            print(board[i][j], end=' ')
        print('|', end='\n')
    print('- - - - - - - - - - - - -', end='\n')


def reading_sudoku():
    """Reading Sudoku from a file"""

    with open("Sudoku", "r") as file:
        sudoku = [[int(j) for j in i.split() if j != '-' and j != '|'] for i in file]
        board = []

        for i in range(len(sudoku)):
            if len(sudoku[i]) != 0:
                board.append(sudoku[i])

        return board





def is_valid(board, num, row, col):
    """Checking whether it is possible to put a number in a cell"""

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    """Solving Sudoku using an backtracking algorithm"""

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

if __name__ == '__main__':
    board = reading_sudoku()
    print("The initial board:")
    writing_sudoku(board)
    solve_sudoku(board)
    print("Solved board:")
    writing_sudoku(board)