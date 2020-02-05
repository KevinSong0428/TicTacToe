#Kevin Song
# CS-UY 1114
# Tic Tac Toe Final project

import turtle
import time
import random
import math

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def draw_board(board):
    turtle.clear()
    turtle.pu()
    turtle.goto(-375, 375)
    turtle.pd()
    turtle.forward(750)
    turtle.right(90)
    turtle.forward(750)
    turtle.right(90)
    turtle.forward(750)
    turtle.right(90)
    turtle.forward(750)
    turtle.pu()
    turtle.goto(-125, -375)
    turtle.pd()
    turtle.forward(750)
    turtle.pu()
    turtle.goto(125, -375)
    turtle.pd()
    turtle.forward(750)
    turtle.pu()
    turtle.right(90)
    turtle.goto(-375, 125)
    turtle.pd()
    turtle.forward(750)
    turtle.pu()
    turtle.goto(-375, -125)
    turtle.pd()
    turtle.forward(750)
    turtle.pu()
    def draw_circle():
        turtle.color("red")
        turtle.pd()
        turtle.circle(125)
        turtle.pu()
        turtle.color("black")
    def draw_x():
        turtle.color("blue")
        diagonal = math.sqrt((250**2)+(250**2))
        turtle.pd()
        turtle.left(135)
        turtle.forward(diagonal)
        turtle.right(135)
        turtle.color("black")
        turtle.forward(250)
        turtle.color("blue")
        turtle.right(135)
        turtle.forward(diagonal)
        turtle.left(135)
        turtle.pu()
        turtle.color("black")
    for box in range(len(board)):
        if board[box] == "O":
            x = -250 + 250 * (box % 3)
            y = 125 - 250 * (box // 3)
            turtle.goto(x,y)
            draw_circle()
        if board[box] == "X":
            x = -125 + 250 * (box % 3)
            y = 125 - 250 * (box // 3)
            turtle.goto(x, y)
            draw_x()
    turtle.update()
    print(the_board)
    
def do_user_move(board, x, y):
    boxes = {-375 < x < -125 and 125 < y < 375 : 0,
             -125 < x < 125 and 125 < y < 375 : 1,
             125 < x < 375 and 125 < y < 375 : 2,
             -375 < x < -125 and -125 < y < 125 : 3,
             -125 < x < 125 and -125 < y < 125 : 4,
             125 < x < 375 and -125 < y < 125 : 5,
             -375 < x < -125 and -375 < y < -125 : 6,
             -125 < x < 125 and -375 < y < -125 : 7,
             125 < x < 375 and -375 < y < -125 : 8,
             x > 375 or x < -375 or y > 375 or y < -375 : 9}
    choice = "O"
    print("user clicked at "+str(x)+","+str(y))
    try:
        for key, val in boxes.items():
                if key:
                    if the_board[int(val)] == "_":
                        the_board[int(val)] = choice
                        turtle.pu()
                        return True
    except IndexError:
        return False

def check_game_over(board):
    player_won = False
    bot_won = False
    stalemate = False
    game_over = False
    stalemate = False
    for i in range(0, 7):       #rows
        if i % 3 == 0 and the_board[i] == "O" and the_board[i] == the_board[i + 1] and the_board[i + 1] == the_board[i + 2]:
            player_won = True
        if i % 3 == 0 and the_board[i] == "X" and the_board[i] == the_board[i + 1] and the_board[i + 1] == the_board[i + 2]:
            bot_won = True
    for i in range(0, 3):       #columns
        if the_board[i] == "O" and the_board[i] == the_board[i + 3] and the_board[i + 3] == the_board[i + 6]:
            player_won = True
        if the_board[i] == "X" and the_board[i] == the_board[i + 3] and the_board[i + 3] == the_board[i + 6]:
            bot_won = True
    if ((the_board[0] == "O" and the_board[0] == the_board[4] and the_board[4] == the_board[8]) or      #diagonal
        (the_board[2] == "O" and the_board[2] == the_board[4] and the_board[4] == the_board[6])):
        player_won = True
    if ((the_board[0] == "X" and the_board[0] == the_board[4] and the_board[4] == the_board[8]) or      #diagonal
        (the_board[2] == "X" and the_board[2] == the_board[4] and the_board[4] == the_board[6])):
        bot_won = True
    if (the_board[0] != "_" and the_board[1] != "_" and the_board[2] != "_" and the_board[3]!= "_" and
        the_board[4] != "_" and the_board[5] != "_" and the_board[6] != "_"and the_board[7] != "_" and
        the_board[8]!= "_" and bot_won == False and player_won == False):
        stalemate = True
    if player_won:
        game_over = player_won
        turtle.goto(-150, 0)
        turtle.write("You Won!", "left", font = ("Comic Sans MS", 50))
    if bot_won:
        game_over = bot_won
        turtle.goto(-295, 0)
        turtle.write("You Lost! Try again!", "left", font = ("Comic Sans MS", 50))
    if stalemate:
        game_over = stalemate
        turtle.goto(-295, 0)
        turtle.write("You tied! Try again!", "left", font = ("Comic Sans MS", 50))
    if game_over:
        turtle.clear()
        time.sleep(2)
        for i in range(len(the_board)):
            the_board[i] = "_"
        draw_board(board)
    return game_over

def check_temp(board):
    for i in range(0, 7):       #rows
        if (i % 3 == 0 and board[i] == "O" and board[i] == board[i + 1] and board[i + 1] == board[i + 2] or
            i % 3 == 0 and board[i] == "X" and board[i] == board[i + 1] and board[i + 1] == board[i + 2]):
            return True
    for i in range(0, 3):       #columns
        if (board[i] == "O" and board[i] == board[i + 3] and board[i + 3] == board[i + 6] or
            board[i] == "X" and board[i] == board[i + 3] and board[i + 3] == board[i + 6]):
            return True
    if ((board[0] == "O" and board[0] == board[4] and board[4] == board[8]) or      #diagonal
        (board[2] == "O" and board[2] == board[4] and board[4] == board[6])):
        return True
    if ((board[0] == "X" and board[0] == board[4] and board[4] == board[8]) or      #diagonal
        (board[2] == "X" and board[2] == board[4] and board[4] == board[6])):
        return True

def do_computer_move(board):
    bot_move = "X"
    valid_move = False
    temp_board = board.copy()
    comp = 0
    player = 0
    while valid_move == False and comp < len(the_board):        #Computer's attempt to win with next move
        if temp_board[comp] == "_":
            temp_board[comp] = "X"
            if check_temp(temp_board):
                valid_move = True
                the_board[comp] = bot_move
            else:
                temp_board[comp] = "_"
        comp += 1
    while valid_move == False and player < len(the_board):      #Trying to block player from winning
        if temp_board[player] == "_":
            temp_board[player] = "O"
            if check_temp(temp_board):
                valid_move = True
                the_board[player] = bot_move
            else:
                temp_board[player] = "_"
        player += 1    
    while valid_move == False:                                  #Computer makes random move
        box = random.randint(0,8)
        if the_board[box] == "_":
            the_board[box] = bot_move
            valid_move = True
    
def clickhandler(x, y):
    if do_user_move(the_board,x,y):             #player move
        draw_board(the_board)                   #draws move
        if not check_game_over(the_board):      #checks if move made by player = win
            do_computer_move(the_board)         #bot move
            draw_board(the_board)               #draws move
            check_game_over(the_board)          #checks if move made by bot = win
            
def main():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()
    
main()
