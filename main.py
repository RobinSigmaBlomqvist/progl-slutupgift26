import random
board = []

rätt=0

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

ship1_row = random_row(board)
ship1_col = random_col(board)
ship2_row = ship1_row + random.randint(-1,1)
ship2_col = ship1_col + random.randint(-1,1)

while True:
    guess_row = int(input("Guess Row:"))-1
    guess_col = int(input("Guess Col:"))-1


    if guess_row == ship1_row and guess_col == ship1_col:
        board[guess_row][guess_col] = '+'
        print_board(board)
        print("Wow du träffa mitt skäpp!")
        rätt+1
    elif guess_row == ship2_row and ship2_col:
        board[guess_row][guess_col] = '+'
        print_board(board)
        print("Wow du träffa mitt skäpp!")
        rätt + 1
    else:
        board[guess_row][guess_col] = 'X'
        print("You missed my battleship!")
        print_board(board)
    if rätt==2:
        print('Du vann, good boy')
        break