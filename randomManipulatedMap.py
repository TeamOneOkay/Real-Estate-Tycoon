import sys
import pygame
import random

width = 900
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

ListOfImages = []
count = 0
randomInt = 0

while roomLeft == False:
    # put out the first image as a blank
    # Low Density to None
    randomInt = random.randint(0,0)
    screen.blit(tileList[randomInt], (tileX,tileY))

    tileX += 50
    ListOfImages.append(randomInt)
    
    print(randomInt)
    count = count + 1
    
    if tileX > 500:
        tileX = 3
        tileY += 50
        if tileY > 500:
            roomLeft = True    

finished = False
while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit()

    pygame.display.flip()
