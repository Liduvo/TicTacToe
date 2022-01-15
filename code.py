board = ["-","-","-","-","-","-","-","-","-"]

def dis():
    print("|"+ board[0] + "|" + board[1] + "|" + board[2])
    print("=========")
    print("|" + board[3] + "|" + board[4] + "|" + board[5])
    print("=========")
    print("|" + board[6] + "|" + board[7] + "|" + board[8])

def check(board):
    p1 = "X"
    p2 = "O"
    if board[0] == board [1] == board[2] == p1 or board[0] == board [1] == board[2] == p2:
        return True
    elif board[3] == board [4] == board[5] == p1 or board[3] == board [4] == board[5] == p2:
        return True
    elif board[6] == board [7] == board[8] == p1 or board[6] == board [7] == board[8] == p2:
        return True
    elif board[1] == board [4] == board[7] == p1 or board[1] == board [4] == board[7] == p2:
        return True
    elif board[2] == board [5] == board[8] == p1 or board[3] == board [4] == board[5] == p2:
        return True
    elif board[0] == board [4] == board[8] == p1 or board[0] == board [4] == board[8] == p2:
        return True
    elif board[2] == board [4] == board[6] == p1 or board[2] == board [4] == board[6] == p2:
        return True
    else:
        return False

def inp(board):
    x = int(input("Please enter the position: "))

    if board[x-1] != "-":
        print("Choose another place this place is full")
        return inp(board)

    else:
        return x
player1 = input("Player 1 nane: ")
player2 = input("Player 2 name: ")
dis()
for i in range(9):
    if i%2 == 0:
        x = inp(board)
        board[x-1] = "X"
        dis()
        if check(board):
            print("Player 1 win")
            break
    else:
        x = inp(board)
        board[x - 1] = "O"
        dis()
        if check(board):
            print("Player 2 win")
            break

    print("Finish")
