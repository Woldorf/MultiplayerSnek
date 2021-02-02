import pygame, random, sys
from pygame.locals import *
#Home Brewed Libraries:
import Drawing, Game
from network import Network
pygame.init()

GameHeight = 500
GameWidth = 500

Window = pygame.display.set_mode((GameWidth, GameHeight),0, 16)
pygame.display.set_caption("Isaacs Very Nice Multiplayer Snek Game")

CELLSIZE=20
CellWidth = int(GameWidth / CELLSIZE)
CellHeight = int(GameHeight / CELLSIZE)

TicksPerSecCLOCK = pygame.time.Clock()

#             R    G    B
GRAY      = (100, 100, 100)
NAVYBLUE  = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)
BLACK     = (  0,   0,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
RAINBOW   = [  0,  85, 170]

#Sound Objects:
#Eating apple sound effect:
EatingAppleSound = pygame.mixer.Sound("SNEK_Sounds/EatingApple.wav")
EatingAppleChannel = pygame.mixer.Channel(1)
#System music:
GameMusicSound = pygame.mixer.Sound("SNEK_Sounds/GameMusic.wav")
GameMusicChannel = pygame.mixer.Channel(2)
#Winner apple sould:
WinnerAppleSound = pygame.mixer.Sound("SNEK_Sounds/WinningApple.wav")

#Set game music volume lower:
GameMusicChannel.set_volume(0.2)

#System functions:
def terminate():
    pygame.quit()
    sys.exit()

Network = Network()

Player = Network.connect()

while True:
    MeSnek,OtherSnek,game = Network.GetData()

    GameWidth,GameHeight = game.GetBoard()
    Window = pygame.display.set_mode((GameWidth, GameHeight),0,32)

    TicksPerSec = game.GetTPS()

    for event in pygame.event.get(): 
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if (MeSnek.Ready == False):
                if (event.key == K_RETURN):
                    MeSnek.Ready = True
            if MeSnek.Ready and OtherSnek.Ready:
                if (event.key == K_LEFT or event.key == K_j) and (MeSnek[Player].Direction != "Right"):
                    MeSnek.Direction = "Left"
                elif (event.key == K_RIGHT or event.key == K_l) and (MeSnek[Player].Direction != "Left"):
                    MeSnek.Direction = "Right"
                elif (event.key == K_UP or event.key == K_i)  and (MeSnek[Player].Direction != "Down"):
                    MeSnek.Direction = "Up"
                elif (event.key == K_DOWN or event.key == K_k) and (MeSnek[Player].Direction != "Up"):
                    MeSnek.Direction = "Down"

    if (MeSnek.Ready == True) and (OtherSnek.Ready == True):
        if game.AppleLocation["Type"] == "Normal":
            AppleColor = RED
        elif game.AppleLocation["Type"] == "Speed":
            AppleColor = YELLOW
        elif game.AppleLocation["Type"] == "Board":
            AppleColor = BLUE

        Drawing.DrawGrid(Window,GameWidth,GameHeight)
        Drawing.DrawSNEK(Window,MeSnek.Cords,MeSnek.Color,MeSnek.InnerColor)
        Drawing.DrawSNEK(Window,OtherSnek.Cords,OtherSnek.Color,OtherSnek.InnerColor)
        Drawing.DrawScores(Window,"LEFT",MeSnek.Cords,GameWidth)
        Drawing.DrawScores(Window,"RIGHT",OtherSnek.Cords,GameWidth)
        Drawing.DrawApple(Window,game.AppleLocation,AppleColor)

    elif (MeSnek.Ready == False) or (OtherSnek.Ready == False):
        Drawing.DrawGrid(Window,GameWidth,GameHeight)

        if Player == 0:
            Drawing.DrawStartScreen(Window,GameWidth,GameHeight,Player)
        else:
            Drawing.DrawStartScreen(Window,GameWidth,GameHeight,Player)

    Network.send(MeSnek.Direction,MeSnek.Ready,Player)
    pygame.display.update()
    TicksPerSecCLOCK.tick(TicksPerSec)