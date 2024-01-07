#~1cherry-trees
def solve_sudoku(board):
    # Find the next empty cell
    row, col = find_empty_cell(board)
    # If there are no empty cells, the board is solved
    if row is None:
        return True
    # Try all possible numbers for this cell
    for num in get_possible_numbers(board, row, col):
        board[row][col] = num
        # Recursively solve the rest of the board
        if solve_sudoku(board):
            return True
        # If the solution was not found, backtrack
        board[row][col] = 0
    # If none of the numbers worked, the board is unsolvable
    return False
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return (None, None)
def get_possible_numbers(board, row, col):
    # Find all numbers in the same row, column, and box
    used_nums = set(board[row]) | set(board[i][col] for i in range(9)) | get_box_numbers(board, row, col)
    # Return the set difference between all numbers and used numbers
    return set(range(1, 10)) - used_nums
def get_box_numbers(board, row, col):
    box_row = row // 3
    box_col = col // 3
    return set(board[box_row * 3 + i][box_col * 3 + j] for i in range(3) for j in range(3) if board[box_row * 3 + i][box_col * 3 + j] != 0)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#testing
solve_sudoku(board)
for row in board:
    print(row)
