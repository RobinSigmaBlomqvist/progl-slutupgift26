import random
import os
board = []

skep1träff = False
skep2träff = False
badpoints = 0
storlek = int(input("Hur stor karta vill du spela? (rekomenderat 5 max 61 helst)"))
pointlimit = storlek*storlek

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

    if 0 <= ship2_row < storlek and 0 <= ship2_col < storlek and (ship1_row != ship2_row or ship1_col != ship2_col):
        break

while True:
    try:
        guess_row = int(input("Guess Row:"))-1
    except(ValueError):
        print("Wrong input buddy")
        continue
    try:
        guess_col = int(input("Guess Col:"))-1
    except(ValueError):
        print("Wrong input buddy")
        continue
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
        if badpoints >= pointlimit * 0.8:
            print("Du suger")
            break
        elif badpoints >= pointlimit * 0.44:
            print("Du van")
            break
        elif badpoints == 6 or badpoints == 7 or badpoints == 67:
            print("SIX SEVEN")
            break
        elif badpoints >=pointlimit * 0.16:
            print("Du vinnen, guten pojken")
            break
        else:
            print("Wow skib-maister du äger")
            break