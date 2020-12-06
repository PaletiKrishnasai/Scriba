import threading 
import time
import os
import random

############################################
##      FUNCTIONS TO MANIPULATE BOARD     ##
############################################

#INIT THE BOARD
def binit(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = 3*i+j+1

#PRINT BOARD IN GIVEN FORMAT
def bprint(board):
    for i in range(3):
        for j in range(3):   
            print(board[i][j],end="")
            if(j<2):
                print("|",end="")
        print()

def HasSpace(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==i*3+j+1):
                return(1)
    return(0)

############################################
## FUNCTIONS TO CHECK FOR A WINNING STATE ##
############################################

#ROW CHECK
def rowCheck(board,out):
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2]):
            out[0] = board[i][0]
            return(1)
    out[0] = 0
    return(0)

#COLUMN CHECK
def colCheck(board,out):
    for i in range(3):
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i]):
            out[1] = board[0][i]
            return(1)    

    out[1] = 0
    return(0)

#DIAGONAL CHECK
def diagCheck(board,out):
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2]):
        out[2] = board[0][0]
        return(1)

    if(board[0][2]==board[1][1] and board[1][1]==board[2][0]):
        out[2] = board[0][2]
        return(1)

    out[2] = 0
    return(0)

############################################
##     MULTITHREADED CHECK FUNCTIONS      ##
############################################
def HasWon(board):
    buffer = [0 for i in range(3)]

    rowCheck(board,buffer)
    colCheck(board,buffer)
    diagCheck(board,buffer)

    for i in buffer:
        if(i != 0):
            return(i)

############################################
##                   AI                   ##
############################################
def copy(a):
    new = [[a[i][0],a[i][1],a[i][2]] for i in range(3)]
    return new

def makeMove(board,pos,player):
    board[int((pos-1)/3)][(pos-1)%3]= player

def moveAvail(board):
    avail = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == (3*i+j)+1):
                avail.append(board[i][j])
    return avail

#max: bool, board: 2D matrix     
def minmax(maxim,board):
    player='X'
    if(maxim):
        player='O'

    if(HasWon(board)):
        if(HasWon(board)=='O'):
            return(1)
        elif(HasWon(board)=='X'):
            return(-1)
    elif(not(HasSpace(board))):
        return(0)
    else:
        scores = []
        for i in moveAvail(board):
            makeMove(board,i,player)
            scores.append(minmax(not(maxim),board))
            makeMove(board,i,i)
            if(scores[-1] == 1 and maxim):
                break
            elif(scores[-1] == -1 and not(maxim)):
                break

        return max(scores) if maxim else min(scores)

def runner(board,res):
    res.append(minmax(False,board))

def Choose(board):
    score = []
    moves = moveAvail(board)
    T = []
    for i in moves:
        boardCpy = copy(board)
        makeMove(boardCpy,i,"O")
        score.append(minmax(False,boardCpy))

    return moves[score.index(max(score))]

############################################
##               MAIN GAME                ##
############################################
def game(board,inputs):
    binit(board)
    pos = -1

    bprint(board)

    while 1:

        while(1):
            inputs[0] = -1
            while inputs[0] == -1:
                time.sleep(0.25)
            pos=inputs[0]
            if (pos>0 and pos<10 and board[int((pos-1)/3)][(pos-1)%3]==pos):
                board[int((pos-1)/3)][(pos-1)%3]= 'X'
                break
            else:
                print("ILLEGAL MOVE!")
                continue

        bprint(board)
        time.sleep(0.05)

        if(HasWon(board)):
            print("-"*80)
            print("X Has won!")
            print("-"*80)
            break

        if(not(HasSpace(board))):
            print("-"*80)
            print("Draw!.......restarting")
            print("-"*80)
            time.sleep(0.5)
            binit(board)
            bprint(board)
            time.sleep(0.25)
            continue

        while(1):
            pos=random.randint(0,9)
            #pos = Choose(board)
            if (pos>0 and pos<10 and board[int((pos-1)/3)][(pos-1)%3]==pos):
                board[int((pos-1)/3)][(pos-1)%3]= 'O'
                print("Played at: ",pos)
                break
            else:
                print("ILLEGAL MOVE!")
                continue
        
        bprint(board)

        if(HasWon(board)):
            print("-"*80)
            print("O Has won!")
            print("-"*80)
            break

