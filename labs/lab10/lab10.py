"""
Name: Duha Kanjo
lab10.py
"""

def build():
    return list(range(1, 10))

def place(board, position, piece):
    if piece == "x" or piece == "o" :
        board[position-1]= piece

def display(board):
    for i in range(3):
        n = i*3
        print(board[n], board[n+1], board[n+2], sep="|")
        print(10*"_")


def isWon(board,piece):
    for i in range(3):
        n = i*3
        if board[n] != piece or board[n+1] != piece or board[n+2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece or board[i+3] != piece or board[i+6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False

def legal(board, position):
    if position >= 1 and position <= 9 and board[position-1] == position:
        return True
    return False

def over(board):
    if isWon(board, "x"):
        return True
    elif isWon(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i+1:
                return False
        return True

def play():
    board = build()

    while True:
        display(board)
        position = eval(input("Enter Position: "))
        if legal(board, position):
            place(board, position, "x")
            display(board)
            if over(board):
                if isWon(board, "x"):
                    print("x won")
                    break
                else:
                    print("Tie")
                    break
        display(board)
        position = eval(input("Enter Position: "))
        if legal(board, position):
            place(board, position, "o")
            display(board)
            if over(board):
                if isWon(board, "o"):
                    print("o won")
                    break
                else:
                    print("Tie")
                    break






def main():
    # add other function calls here
    play()


main()
