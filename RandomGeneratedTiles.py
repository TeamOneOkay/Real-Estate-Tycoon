import sys
import pygame
import random
import os

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
OMedLowTile = pygame.image.load("LowAndMedComp.png").convert()
OMedMedTile = pygame.image.load("MedAndMedComp.png").convert()
OMedHighTile = pygame.image.load("HighAndMedComp.png").convert()
ORichLowTile = pygame.image.load("LowAndRichComp.png").convert()
ORichMedTile = pygame.image.load("MedAndRichComp.png").convert()
ORichHighTile = pygame.image.load("HighAndRichComp.png").convert()


tileList = [blankTile,
            PoorLowTile, PoorMedTile, PoorHighTile,
            MedLowTile, MedMedTile, MedHighTile,
            RichLowTile, RichMedTile, RichHighTile,
            PPoorLowTile, PPoorMedTile, PPoorHighTile,
            PMedLowTile, PMedMedTile, PMedHighTile,
            PRichLowTile, PRichMedTile, PRichHighTile,
            OPoorLowTile, OPoorMedTile, OPoorHighTile,
            OMedLowTile, OMedMedTile, OMedHighTile,
            ORichLowTile, ORichMedTile, ORichHighTile           
            ]

while roomLeft == False:    
    
    screen.blit(tileList[random.randint(0,27)], (tileX,tileY))
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

    pygame.display.flip()
