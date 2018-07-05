import sys
import pygame
import random
import os

pygame.init()
#window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

width = 1000
height = 700

screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("Random Grid")

grassTile = pygame.image.load("grassTile.png").convert()

roomLeft = False
tileX = 3
tileY = 3

FPS = 30

# Starting Values for game
one_year = (360 * FPS) # One Game Year
retire = (7200 * FPS) # 20 Game Years
retirement = 20 # 20 years to play game
money = 10000
prof_loss = 0
low = 0
med = 0
hig = 0

#Colors
white_color = (255,255,255)
blue_color = (0,0,255)
toolBar = pygame.image.load("ToolBar.png")
CLOCK = pygame.time.Clock()

screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("Random Grid")

grassTile = pygame.image.load("grassTile.png").convert()

roomLeft = False
tileX = 3
tileY = 3

# Keeps track of the remaining years and time left until retire
def time_keeper():
    global one_year
    global retire
    global retirement 
    if retire > 0:
        if one_year <= 0:
            retirement -= 1
            one_year =  (FPS * 360)
        
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

# Basic Tiles
blankTile = pygame.image.load("grassTile.png").convert()
PoorLowTile = pygame.image.load("LowAndPoor.png").convert()
PoorMedTile = pygame.image.load("MedAndPoor.png").convert()
PoorHighTile = pygame.image.load("HighAndPoor.png").convert()
MedLowTile = pygame.image.load("LowAndMed.png").convert()
MedMedTile = pygame.image.load("MedAndMed.png").convert()
MedHighTile = pygame.image.load("HighAndMed.png").convert()
RichLowTile = pygame.image.load("LowAndRich.png").convert()
RichMedTile = pygame.image.load("MedAndRich.png").convert()
RichHighTile = pygame.image.load("HighAndRich.png").convert()

# Player Tiles
PPoorLowTile = pygame.image.load("LowAndPoorPlayer.png").convert()
PPoorMedTile = pygame.image.load("MedAndPoorPlayer.png").convert()
PPoorHighTile = pygame.image.load("HighAndPoorPlayer.png").convert()
PMedLowTile = pygame.image.load("LowAndMedPlayer.png").convert()
PMedMedTile = pygame.image.load("MedAndMedPlayer.png").convert()
PMedHighTile = pygame.image.load("HighAndMedPlayer.png").convert()
PRichLowTile = pygame.image.load("LowAndRichPlayer.png").convert()
PRichMedTile = pygame.image.load("MedAndRichPlayer.png").convert()
PRichHighTile = pygame.image.load("HighAndRichPlayer.png").convert()

# Computer Opponet Tiles
OPoorLowTile = pygame.image.load("LowAndPoorComp.png").convert()
OPoorMedTile = pygame.image.load("MedAndPoorComp.png").convert()
OPoorHighTile = pygame.image.load("HighAndPoorComp.png").convert()
#OMedLowTile = pygame.image.load("LowAndMedComp.png").convert()
#OMedMedTile = pygame.image.load("MedAndMedComp.png").convert()
#OMedHighTile = pygame.image.load("HighAndMedComp.png").convert()
#ORichLowTile = pygame.image.load("LowAndRichComp.png").convert()
#ORichMedTile = pygame.image.load("MedAndRichComp.png").convert()
#ORichHighTile = pygame.image.load("HighAndRichComp.png").convert()


tileList = [blankTile,
            PoorLowTile, PoorMedTile, PoorHighTile,
            MedLowTile, MedMedTile, MedHighTile,
            RichLowTile, RichMedTile, RichHighTile,
            PPoorLowTile, PPoorMedTile, PPoorHighTile,
            PMedLowTile, PMedMedTile, PMedHighTile,
            PRichLowTile, PRichMedTile, PRichHighTile,
            OPoorLowTile, OPoorMedTile, OPoorHighTile
 #           OMedLowTile, OMedMedTile, OMedHighTile,
 #           ORichLowTile, ORichMedTile, ORichHighTile           
            ]

while roomLeft == False:    
    
    screen.blit(tileList[random.randint(0,21)], (tileX,tileY))
    tileX += 45
    
    if tileX > 600:
        tileX = 3
        tileY += 35
        if tileY > 600:
            roomLeft = True

    

finished = False
while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit()

    screen.blit(toolBar,(0,0))
    time_keeper()
    game_score_keeper()
    CLOCK.tick(FPS)

    pygame.display.flip()
