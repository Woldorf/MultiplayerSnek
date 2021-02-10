import pygame, random, sys
from pygame.locals import *
#Home Brewed Libraries:
import Drawing
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
Player = Network.Connect()

while True:
    Sneks,game = Network.Get()
    if Player == 1:
        MeSnek = Sneks[1]
        OtherSnek = Sneks[0]
    else:
        MeSnek = Sneks[0]
        OtherSnek = Sneks[1]

    GameWidth,GameHeight = game.GetBoard()
    Window = pygame.display.set_mode((GameWidth, GameHeight),0,32)

    TicksPerSec = game.GetTPS()

    for event in pygame.event.get(): 
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if not MeSnek.Ready:
                if (event.key == K_RETURN):
                    MeSnek.Ready = True
            if MeSnek.Ready and OtherSnek.Ready:
                if (event.key == K_a) and (MeSnek.Direction != "Right"):
                    MeSnek.Direction = "Left"
                elif (event.key == K_d) and (MeSnek.Direction != "Left"):
                    MeSnek.Direction = "Right"
                elif (event.key == K_w)  and (MeSnek.Direction != "Down"):
                    MeSnek.Direction = "Up"
                elif (event.key == K_s) and (MeSnek.Direction != "Up"):
                    MeSnek.Direction = "Down"

    if MeSnek.Ready and OtherSnek.Ready:
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

        print(MeSnek.Direction,OtherSnek.Direction)

    elif not (MeSnek.Ready and OtherSnek.Ready):
        Drawing.DrawGrid(Window,GameWidth,GameHeight)
        Drawing.DrawStartScreen(Window,GameWidth,GameHeight,Player)

        Drawing.DrawSNEK(Window,MeSnek.Cords,MeSnek.Color,MeSnek.InnerColor)
        Drawing.DrawSNEK(Window,OtherSnek.Cords,OtherSnek.Color,OtherSnek.InnerColor)

    Network.Send(MeSnek.Direction,MeSnek.Ready,Player)
    pygame.display.update()
    TicksPerSecCLOCK.tick(TicksPerSec)