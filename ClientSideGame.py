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


Network = Network()

Player = Network.connect()
print("You're player #" + str(int(Player) +1))

Drawing.DrawGrid(Window,GameWidth,GameHeight)
if Player == 0:
    Drawing.DrawStartScreen(Window,GameWidth,GameHeight,Player)
else:
    Drawing.DrawStartScreen(Window,GameWidth,GameHeight,Player)

Players,game = Network.GetData()

for event in pygame.event.get(): 
    if event.type == QUIT:
        break
    elif event.type == KEYDOWN:
        if event.key == K_KP_ENTER:
            if Player == 0:
                game.P1Ready = True
            else:
                game.P2Ready = True

while True:
    GameWidth,GameHeight = game.GetBoard(CELLSIZE)
    Window = pygame.display.set_mode((GameWidth, GameHeight),0, 16)

    TicksPerSec = game.GetTPS()

    for event in pygame.event.get(): 
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            #Snek 1 direction settings:
            if (event.key == K_LEFT or event.key == K_j) and (Players[Player].Direction != "Right"):
                Players[Player].Direction = "Left"
            elif (event.key == K_RIGHT or event.key == K_l) and (Players[Player].Direction != "Left"):
                Players[Player].Direction = "Right"
            elif (event.key == K_UP or event.key == K_i)  and (Players[Player].Direction != "Down"):
                Players[Player].Direction = "Up"
            elif (event.key == K_DOWN or event.key == K_k) and (Players[Player].Direction != "Up"):
                Players[Player].Direction = "Down"

    Snek1 = Players[0]
    Snek2 = Players[1]

    Drawing.DrawGrid(Window,GameWidth,GameHeight)
    Drawing.DrawSNEK(Window,Snek1.Cords,Snek1.Color,Snek1.InnerColor)
    Drawing.DrawSNEK(Window,Snek2.Cords,Snek2.Color,Snek1.InnerColor)
    Drawing.DrawScores(Window,"LEFT",Snek1.Cords,GameWidth)
    Drawing.DrawScores(Window,"RIGHT",Snek2.Cords,GameWidth)
    Drawing.DrawApple(Window,game.AppleLocation,game.AppleColor)
    
    Players, game = Network.send(Players,game)
    TicksPerSecCLOCK.tick(TicksPerSec)