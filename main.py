import random
import os
board = []

rätt = 0
badpoints = 0
place = True
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
while place==True:
    ship1_row = random_row(board)
    ship1_col = random_col(board)
    ship2_row = ship1_row + random.randint(-1,1)
    ship2_col = ship1_col + random.randint(-1,1)
    
    if ship2_row >= 1 and ship2_row <= 5 and ship2_col >= 1 and ship2_col <= 5:
        place == False

while True:
    guess_row = int(input("Guess Row:"))-1
    guess_col = int(input("Guess Col:"))-1
    os.system('cls')

    if guess_row == ship1_row and guess_col == ship1_col:
        board[guess_row][guess_col] = '+'
        print_board(board)
        print("Wow du träffa mitt skäpp!")
        rätt += 1
    elif guess_row == ship2_row and guess_col == ship2_col:
        board[guess_row][guess_col] = '+'
        print_board(board)
        print("Wow du träffa mitt skäpp!")
        rätt += 1
    else:
        board[guess_row][guess_col] = 'X'
        print_board(board)
        print("You missed my battleship!")
        badpoints += 1
    if rätt >= 2:
        if badpoints>=20:
            print("Du suger")
        elif badpoints >= 11:
            print("Du van, men dåligt")
        elif badpoints == 6 or badpoints ==7:
            print("SIX or SEVEN")
        elif badpoints >=4:
            print("Die vinnen, guten pojken")
        else:
            print("Wow skib-maister du äger")
