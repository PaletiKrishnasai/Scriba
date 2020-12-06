import TicTacToe as ttc
import os
import threading
import sys
from p5 import *

board = [[3*i+1,3*i+2,3*i+3] for i in range(3)]
mousePos = [-1]

def setup():
    size(543, 543)

def draw():
    global mousePos
    stroke_weight(6)
    
#### BOARD ####
    rect((0,0),540,540)
    line(0,180,540,180)
    line(0,360,540,360)
    line(180,0,180,540)
    line(360,0,360,540)

#### PLAYER POSITIONS ####
    variables()

    if mouse_is_pressed:
        mousePos[0] = int((mouse_x)/180) + int((mouse_y)/180)*3 + 1
        

def Xdraw(x,y):
    stroke(0,128,0)
    stroke_weight(8)
    line(x+15,y+15,x+165,y+165)
    line(x+165,y+15,x+15,y+165)   
    stroke_weight(6)
    stroke(0)

def Odraw(x,y):
    stroke(128,0,0)
    stroke_weight(8)
    ellipse(x+90,y+90,160,160)
    stroke_weight(6)
    stroke(0)

def variables():
    global board
    for i in range(3):
        for j in range(3):
            if(board[j][i] == 'X'):
                Xdraw(i*180,j*180)
            elif(board[j][i] == 'O'):
                Odraw(i*180,j*180)

def wrapper(inp):
    for i in range(3):
        for j in range(3):
            board[i][j] = inp[i][j]
    try:
        run()
    except Exception:
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')
            
        raise os._exit(1)

board = [[3*i+1,3*i+2,3*i+3] for i in range(3)]
t1 = threading.Thread(target=ttc.game,args=(board,mousePos))
t2 = threading.Thread(target=wrapper,args=(board,))

t1.start()
t2.start()

t1.join()
time.sleep(1)
os._exit(0)


