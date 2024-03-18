def is_valid(board, row, col, num):
    # Check if the number is already in the row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def solve_sudoku(board):
    row, col = find_empty_cell(board)

    # If there are no empty cells, the Sudoku puzzle is solved
    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If placing num leads to a dead end, backtrack by resetting the cell
            board[row][col] = 0

    return False

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [0, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved:")
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists for the Sudoku puzzle.")
