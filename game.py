import os
import pygame
import random
import time
from random import choices
from random import uniform
from math import exp
from math import ceil
import sys
import csv
import threading

# Define width and height of img
IMG_WIDTH = 48
IMG_HEIGHT = 48

# Define window size
WIN_WIDTH = 780
WIN_HEIGHT = 1024
#WIN_SIZE = (WIN_WIDTH,WIN_HEIGHT)

# Define offset for score display
OFFSET = 80

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 255)
black = (0,0,0)
white = (255,255,255)
BLUE=(176,224,230)
red = (200,0,0)
green = (0,200,0)
pygame.init()

bright_red = (255,0,0)
bright_green = (0,255,0) 
block_color = (53,115,255)

pygame.mixer.init()
pygame.mixer.music.load('assets/music.ogg')
# set volume and play furelise infinitely
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
pygame.font.init()
def quitgame():
    pygame.quit()
    quit()
def text_objects(text, font):
    textSurface = font.render(text, True,WHITE)
    return textSurface, textSurface.get_rect()

def title(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
     #   pygame.draw.rect(screen, ac,(x,y,w,h))
                
        op1surface = pygame.image.load('assets/diff_title.jpg').convert_alpha()
        op1surface = pygame.transform.scale(op1surface, (400,200))
        op1_box = op1surface.get_rect(center = ((x+w/2,y+h/2)))
        screen.blit(op1surface,op1_box)
     
        if click[0] == 1 and action != None:
            action()         
    else:
      #  pygame.draw.rect(screen, ic,(x,y,w,h))
                
        op1surface = pygame.image.load('assets/diff_title.jpg').convert_alpha()
        op1surface = pygame.transform.scale(op1surface, (400,200))
        op1_box = op1surface.get_rect(center = ((x+w/2,y+h/2)))
        screen.blit(op1surface,op1_box)
    #font = pygame.font.Font('assets/fonts/AvenirMedium.ttf', 18)

    smallText = pygame.font.Font('assets/fonts/AvenirMedium.ttf', 26)# pygame.font.SysFont("comicsansms",40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def title_2(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
#        pygame.draw.rect(screen, ac,(x,y,w,h))
                
        op1surface = pygame.image.load('assets/main.jpg').convert_alpha()
        op1surface = pygame.transform.scale(op1surface, (400,200))
        op1_box = op1surface.get_rect(center = ((x+w/2,y+h/2)))
        screen.blit(op1surface,op1_box)

        if click[0] == 1 and action != None:
            action()         
    else:
                
        op1surface = pygame.image.load('assets/main.jpg').convert_alpha()
        op1surface = pygame.transform.scale(op1surface, (400,200))
        op1_box = op1surface.get_rect(center = ((x+w/2,y+h/2)))
        screen.blit(op1surface,op1_box)
    #font = pygame.font.Font('assets/fonts/AvenirMedium.ttf', 18)

    smallText = pygame.font.Font('assets/fonts/AvenirMedium.ttf', 26)# pygame.font.SysFont("comicsansms",40)
    textSurf, textRect = text_objects(msg, smallText)
    #textRect.center = ( (x+(w/2)), (y+(h/2)) )
    #screen.blit(textSurf, textRect)

WIN_HEIGHT = (pygame.display.Info().current_h * 9) // 10
WIN_SIZE = (WIN_WIDTH,WIN_HEIGHT)
screen = pygame.display.set_mode(WIN_SIZE)
snow_list = []

while True:
    bg_surface=pygame.image.load('assets/back.webp').convert_alpha()
    bg_surface = pygame.transform.scale(bg_surface, (WIN_WIDTH,WIN_HEIGHT))
    screen.blit(bg_surface,(0,0))
    
    op1surface = pygame.image.load('assets/tic.jpeg').convert_alpha()
    op1surface = pygame.transform.scale(op1surface, (200,200))
    op1_box = op1surface.get_rect(center = ((WIN_WIDTH/2-10,WIN_HEIGHT/2-50)))
    screen.blit(op1surface,op1_box)
    title_2("M A I N M E N U",190,100,400,150,BLACK,GRAY)

    op2surface = pygame.image.load('assets/text.jpeg').convert_alpha()
    op2surface = pygame.transform.scale(op2surface, (200,200))
    op2_box = op2surface.get_rect(center = ((WIN_WIDTH/2-10,WIN_HEIGHT/2+270)))
    screen.blit(op2surface,op2_box)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if(op2_box.collidepoint(pygame.mouse.get_pos())):
                os.system('python3 EditorMul.py')
                quit()
            if(op1_box.collidepoint(pygame.mouse.get_pos())):
                back=1
                while (back==1):
                
                    screen.fill(black)
                    bg_surface=pygame.image.load('assets/tic_b.jpeg').convert_alpha()
                    bg_surface = pygame.transform.scale(bg_surface, (WIN_WIDTH,WIN_HEIGHT))
                    screen.blit(bg_surface,(0,0))

                    title("    ",190,100,400,150,BLACK,GRAY)
                    op3surface = pygame.image.load('assets/hard.png').convert_alpha()
                    op3surface = pygame.transform.scale(op3surface, (200,200))
                    op3_box = op3surface.get_rect(center = ((WIN_WIDTH/2+170,WIN_HEIGHT/2+100)))
                    screen.blit(op3surface,op3_box)
                    op4surface = pygame.image.load('assets/easy.jpg').convert_alpha()
                    op4surface = pygame.transform.scale(op4surface, (200,200))
                    op4_box = op4surface.get_rect(center = ((WIN_WIDTH/2-170,WIN_HEIGHT/2)))
                    screen.blit(op4surface,op4_box)
                    op6surface = pygame.image.load('assets/medium.jpg').convert_alpha()
                    op6surface = pygame.transform.scale(op6surface, (200,200))
                    op6_box = op6surface.get_rect(center = ((WIN_WIDTH/2-170,WIN_HEIGHT/2+300)))
                    screen.blit(op6surface,op6_box)
                    
                    op5surface = pygame.image.load('assets/goback.png').convert_alpha()
                    op5surface = pygame.transform.scale(op5surface, (75,70))
                    op5_box = op5surface.get_rect(center = ((WIN_WIDTH/2-350,WIN_HEIGHT/2+400)))
                    screen.blit(op5surface,op5_box)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.MOUSEBUTTONUP:
                            if(op4_box.collidepoint(pygame.mouse.get_pos())):
                                os.system('python3 ./Random/main.py')
                            if(op3_box.collidepoint(pygame.mouse.get_pos())):
                                os.system('python3 ./MiniMax/main.py')
                            if(op6_box.collidepoint(pygame.mouse.get_pos())):
                                os.system('python3 ./Medium/main.py')
                            
                            if(op5_box.collidepoint(pygame.mouse.get_pos())):
                                screen.fill(black)
                                back=0
                    pygame.display.update()
                    
                #os.system('python3 .....py')
                #quit()
    
    pygame.display.update()
