import random

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def display_board(board):
    for row in board:
        print(' '.join(str(cell).rjust(4) if cell != 0 else '.'.rjust(4) for cell in row))
    print()

def merge(row):
    merged_row = []
    i = 0
    while i < len(row):
        if i + 1 < len(row) and row[i] == row[i + 1]:
            merged_row.append(row[i] * 2)
            i += 2
        else:
            merged_row.append(row[i])
            i += 1
    merged_row += [0] * (len(row) - len(merged_row))
    return merged_row

def move(board, direction):
    if direction == 'up':
        board = [list(x) for x in zip(*board)]
        board = [merge(row) for row in board]
        board = [list(x) for x in zip(*board)]
    elif direction == 'down':
        board = [list(x) for x in zip(*board[::-1])]
        board = [merge(row) for row in board]
        board = [list(x) for x in zip(*board)][::-1]
    elif direction == 'left':
        board = [merge(row) for row in board]
    elif direction == 'right':
        board = [row[::-1] for row in board]
        board = [merge(row) for row in board]
        board = [row[::-1] for row in board]
    return board

def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
        for i in range(3):
            if row[i] == row[i + 1]:
                return False
    return True

def main():
    print("Welcome to 2048!")
    print("Slide the tiles with 'up', 'down', 'left', or 'right' arrow keys.")
    print("Join the numbers and get to the 2048 tile!")
    print("Good luck!\n")
    
    board = initialize_board()
    while True:
        display_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        direction = input("Enter move (up/down/left/right): ").lower()
        if direction in ('up', 'down', 'left', 'right'):
            board = move(board, direction)
            add_new_tile(board)
        else:
            print("Invalid move! Please enter 'up', 'down', 'left', or 'right'.")

if __name__ == "__main__":
    main()
