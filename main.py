import random
import os
board = []

skep1träff = False
skep2träff = False
badpoints = 0
storlek = int(input("Hur stor karta vill du spela? (rekomenderat 5 max 61 helst)"))

for x in range(0,storlek):
    board.append(["O"] * storlek)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

while True:
    ship1_row = random_row(board)
    ship1_col = random_col(board)
    ship2_row = ship1_row + random.randint(-1,1)
    ship2_col = ship1_col + random.randint(-1,1)

    if ship2_row >= 0 and ship2_row <= len(board) - 1 and ship2_col >= 0 and ship2_col <= len(board) - 1 and (ship2_row != ship1_row or ship2_col != ship1_col):
        break

while True:
    guess_row = int(input("Guess Row:"))-1
    guess_col = int(input("Guess Col:"))-1
    os.system('cls')

    if guess_row == ship1_row and guess_col == ship1_col:
        board[guess_row][guess_col] = '+'
        print_board(board)
        print("Wow du träffa mitt skäpp!")
        skep1träff = True
    elif guess_row == ship2_row and guess_col == ship2_col:
        board[guess_row][guess_col] = '+'
        print_board(board)
        print("Wow du träffa mitt skäpp!")
        skep2träff = True
    else:
        board[guess_row][guess_col] = 'X'
        print_board(board)
        print("You missed my battleship!")
        badpoints += 1

    if skep1träff == True and skep2träff == True:
        if badpoints>=20:
            print("Du suger")
            break
        elif badpoints >= 11:
            print("Du van")
            break
        elif badpoints == 6 or badpoints ==7:
            print("SIX or SEVEN")
            break
        elif badpoints >=4:
            print("Du vinnen, guten pojken")
            break
        else:
            print("Wow skib-maister du äger")
            break