from tkinter import *
import copy

root = Tk()
root.geometry("340x500")
root.title("Tic Tac Toe")

root.resizable(0,0)

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial" , 26) , bg="orange" , width=16 )
titleLabel.grid(row=0 , column=0)

frame2 = Frame(root , bg="pink")
frame2.pack()

board = { 1:" " , 2:" " , 3:" ",
          4:" " , 5:" " , 6:" ",
          7:" " , 8:" " , 9:" " }

turn = "X"
game_end = False


def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"] = board[key]

def checkForWin(player):
    print(board)
    board_1d = []
    for key in board.keys():
        board_1d.append(board[key])
    
    two_d_board = [board_1d[i:i + 3] for i in range(0, len(board_1d), 3)]

    # Check rows, columns, for a win
    for i in range(3):
        if all(two_d_board[i][j] == player for j in range(3)) or all(two_d_board[j][i] == player for j in range(3)):
            return True
        
    # Check diagonals for a win
    if all(two_d_board[i][i] == player for i in range(3)) or all(two_d_board[i][2 - i] == player for i in range(3)):
        return True
    return False
    
    # Other way for checking the terminal state
    # rows
    # if board[1] == board[2] and board[2] == board[3] and board[3] == player:
    #     return True
    
    # elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
    #     return True
    
    # elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
    #     return True

    # # columns
    # elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
    #     return True
    
    # elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
    #     return True
    
    # elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
    #     return True
    
    # # diagonals
    # elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
    #     return True
    
    # elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
    #     return True
    

    return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    
    return True

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial" , 30) , bg="orange" , width=15 )
    titleLabel.grid(row=0 , column=0)

def minimax(board , isMaximizing):
    
    if checkForWin("O"):
        return 1 
    
    if checkForWin("X"):
        return -1
    
    if checkForDraw():
        return 0
    
    if isMaximizing:
        bestScore = float("-inf")

        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                # print(board)  ############Printing the board
                score = minimax(board , False) # minimax
                board[key] = " "
                if score > bestScore : 
                    bestScore = score 
        
        return bestScore
    
    else:
        bestScore = float("inf")

        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                # print(board)  ############Printing the board
                score = minimax(board , True) # minimax
                board[key] = " "
                if score < bestScore : 
                    bestScore = score 
        
        return bestScore

def playComputer():
    bestScore = float("-inf")
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            score = minimax(board , False) # minimax
            board[key] = " "
            if score > bestScore : 
                bestScore = score 
                bestMove = key

    board[bestMove] = "O"

# Function to play
def play(event):
    global turn,game_end
    if game_end:
        return
    
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n" :
        clicked = 1
    else :
        clicked = int(clicked)
    
    if button["text"] == " ":
        if turn == "X" :
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="orange", font=("Arial" , 26),width=16 )
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                game_end = True

            turn = "O"

            updateBoard()

            playComputer()

            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="orange", font=("Arial" , 26),width=16   )
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                game_end = True

            turn = "X"

            updateBoard()
       
        else:
            board[clicked] = turn
            updateBoard()
            if checkForWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game" , bg="orange", font=("Arial" , 26),width=16)
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                game_end = True
            turn = "X"

        
        if checkForDraw():
            drawLabel = Label(frame1 , text=f"Game Draw" , bg="orange", font=("Arial" , 26), width = 16)
            drawLabel.grid(row = 0 , column=0 , columnspan=3)
        

#  First row 

button1 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5)
button1.grid(row = 0 , column=0)
button1.bind("<Button-1>" , play)

button2 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5 )
button2.grid(row = 0 , column=1)
button2.bind("<Button-1>" , play)

button3 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5 )
button3.grid(row = 0 , column=2)
button3.bind("<Button-1>" , play)

#  second row 

button4 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5 )
button4.grid(row = 1 , column=0)
button4.bind("<Button-1>" , play)

button5 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5 )
button5.grid(row = 1 , column=1)
button5.bind("<Button-1>" , play)

button6 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5 )
button6.grid(row = 1 , column=2)
button6.bind("<Button-1>" , play)

#  third row 

button7 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5)
button7.grid(row = 2 , column=0)
button7.bind("<Button-1>" , play)

button8 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5 )
button8.grid(row = 2 , column=1)
button8.bind("<Button-1>" , play)

button9 = Button(frame2 , text= " " , width=4 , height=2  , font=("Arial" , 30), bg="pink" , relief=RAISED , borderwidth=5)
button9.grid(row = 2 , column=2)
button9.bind("<Button-1>" , play)

restartButton = Button(frame2 , text="Restart Game" , width=19 , height=1 , font=("Arial" , 20) , bg="Green" , relief=RAISED , borderwidth=5 , command=restartGame )
restartButton.grid(row=4 , column=0 , columnspan=3)

buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8, button9]

root.mainloop()