board = { 
    1: "1",
    2: "2",
    3: "3", 
    4: "4", 
    5: "X", 
    6: "6", 
    7: "7", 
    8: "8", 
    9: "9"
}

def DisplayBoard(board):
    
    print ("+-------" * 3, "+", sep="")
    print ("|       " * 3, "|", sep="")
    print ("|   ", board.get(1), "   |   ", board.get(2), "   |   ", board.get(3), "   |", sep = "")
    print ("|       " * 3, "|", sep="")
    print ("+-------" * 3, "+", sep="")
    print ("|       " * 3, "|", sep="")
    print ("|   ", board.get(4), "   |   ", board.get(5), "   |   ", board.get(6), "   |", sep = "")
    print ("|       " * 3, "|", sep="")
    print ("+-------" * 3, "+", sep="")
    print ("|       " * 3, "|", sep="")
    print ("|   ", board.get(7), "   |   ", board.get(8), "   |   ", board.get(9), "   |", sep = "")
    print ("|       " * 3, "|", sep="")
    print ("+-------" * 3, "+", sep="")

DisplayBoard(board)

def UserMove(board):
    move = int(input("Enter your move: "))
    #then uodate the dict
    board[move] = "O"
    DisplayBoard(board) 
UserMove(board)

def DrawMove(board):
    for key, value in board.items():
        if value != "X" and value != "O":
            board[key] = "X"
            break
    DisplayBoard(board)
DrawMove(board)

def FreeSquares(board):
    lst=[]
    for value, key in board.items():
        if key != "X" and key != "O":
            lst.append((value, key))
    return lst

def VictoryFor(board, sign):
    win = False
    if board.get(1) == board.get(4) == board.get(7) == sign\
    or board.get(2) == board.get(5) == board.get(8) == sign\
    or board.get(3) == board.get(6) == board.get(9) == sign\
    or board.get(1) == board.get(2) == board.get(3) == sign\
    or board.get(4) == board.get(5) == board.get(6) == sign\
    or board.get(7) == board.get(8) == board.get(9) == sign\
    or board.get(1) == board.get(5) == board.get(9) == sign\
    or board.get(3) == board.get(5) == board.get(7) == sign:
        win = True
        if sign == "X":
            print ("Game over. Computer wins!!!! ")    
        else:
            print ("Game over. User wins!!!! ")
    if win != True and len(FreeSquares(board)) > 0:
        if sign == "X":
            UserMove(board)
            VictoryFor(board, sign="O")
        if sign =="O":
            DrawMove(board)
            VictoryFor(board, sign="X")      
    elif win != True and len(FreeSquares(board)) == 0: 
        print ("It's a tie")

VictoryFor(board, sign="X")