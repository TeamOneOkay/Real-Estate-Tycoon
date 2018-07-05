import pygame
import math,random,sys
import os
import pylint
from pygame.locals import * 

pygame.init()

#Variable Section
FPS = 1
#screen size
w = 1000
h = 700
screenDim = (w,h)
#x and y values for the screen
x = 0
y = 0
# Starting Values for game
one_year = 20#(360 * FPS) # One Game Year
retire = (7200 * FPS) # 20 Game Years
retirement = 20 # 20 years to play game
money = 10000
prof_loss = 0
low = 0
med = 0
hig = 0

done = False

#Colors
white_color = (255,255,255)
blue_color = (0,0,255)

toolBar = pygame.image.load("ToolBar.png")

CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(screenDim) 
pygame.display.set_caption('Real Estate Tycoon')

# Keeps track of the remaining years and time left until retire
def time_keeper():
    global one_year
    global retire
    global retirement 
    if retire > 0:
        if one_year <= 0:
            retirement -= 1
            one_year = 20#(FPS * 360)
        
        retire -= 30
        one_year -= 1
        
# updates the screen with current play values
def game_score_keeper():
    #Font Type
    font = pygame.font.SysFont("monospace", 30,bold = 1)
    #Locations for the play values
    retire_rect      = pygame.Rect(50,650,150,30)
    money_rect       = pygame.Rect(250,650,150,30)
    profit_loss_rect = pygame.Rect(450,650,150,30)
    low_rect         = pygame.Rect(650,650,50,30)
    med_rect         = pygame.Rect(750,650,50,30)
    hig_rect         = pygame.Rect(850,650,50,30)
    #redering values to strings
    font_retire = font.render(str(retirement),1,blue_color)
    font_money = font.render(str(money),1,blue_color)
    font_prof_loss = font.render(str(prof_loss),1,blue_color)
    font_low = font.render(str(low),1,blue_color)
    font_med = font.render(str(med),1,blue_color)
    font_hig = font.render(str(hig),1,blue_color)
    #Display values onto the screen
    screen.blit(font_retire,retire_rect)
    screen.blit(font_money,money_rect)
    screen.blit(font_prof_loss,profit_loss_rect)
    screen.blit(font_low,low_rect)
    screen.blit(font_med,med_rect)
    screen.blit(font_hig,hig_rect)
    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True

    screen.blit(toolBar,(0,0))
    time_keeper()
    game_score_keeper()
    pygame.display.flip()
    #screen.fill(white_color)
    
    
   
    CLOCK.tick(FPS)
    

    
