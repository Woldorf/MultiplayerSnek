import pygame

CELLSIZE = 20

def DrawGrid(Window, xSize, ySize):
    DARKGREY = ( 40,  40,  40)

    Window.fill((0,0,0))

    for x in range(0, xSize, CELLSIZE): # draw vertical lines
        pygame.draw.line(Window, DARKGREY, (x, 0), (x, ySize))
    for y in range(0, ySize, CELLSIZE): # draw horizontal lines
        pygame.draw.line(Window, DARKGREY, (0, y), (xSize, y))

def DrawSNEK(Window,CordsList,Color,InnerColor):
    HEAD = 0
    ORANGE = (255, 128,   0)

    for cord in CordsList:
        x = cord["x"] * CELLSIZE
        y = cord["y"] * CELLSIZE

        SnekSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        SnekInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)

        if (cord["x"] == CordsList[HEAD]["x"]) and (cord["y"] == CordsList[HEAD]["y"]):
            pygame.draw.rect(Window, Color, SnekSegmentRect)
            pygame.draw.rect(Window, ORANGE, SnekInnerSegmentRect)
        else:
            pygame.draw.rect(Window, Color, SnekSegmentRect)
            pygame.draw.rect(Window, InnerColor, SnekInnerSegmentRect)

def DrawApple(Window,Cords,Color):
    x=Cords['x'] * CELLSIZE
    y=Cords['y'] * CELLSIZE

    FruitRect=pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(Window,Color,FruitRect)

def DrawScores(Window,Side,SnekCords,xSize):
    FONT = pygame.font.Font("freesansbold.ttf",18)
    DARKGREEN = (  0, 155,   0)
    CYAN      = (  0, 255, 255)

    if Side=="LEFT":
        scoreSurf = FONT.render('Snek1 Length: '+str(len(SnekCords)), True, DARKGREEN)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (10,10)
    elif Side=="RIGHT":
        scoreSurf = FONT.render('Snek2 Length: '+str(len(SnekCords)), True, CYAN)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topright = ((xSize -10) , 10)    
    
    Window.blit(scoreSurf, scoreRect)

def DrawStartScreen(Window,xSize,ySize,Player):
    BIGFONT = pygame.font.Font("freesansbold.ttf",26)
    SMALLFONT = pygame.font.Font("freesansbold.ttf",20)
    GREEN     = (  0, 255,   0)
    CYAN      = (  0, 255, 255)

    if Player == 0:
        ControlsWords = SMALLFONT.render("WASD To Move Your GREEN Snek",True,GREEN)
        TitleScreenWords = BIGFONT.render("You are player " + str(Player + 1),True,GREEN)
    else:
        ControlsWords = SMALLFONT.render("WASD To Move Your BLUE Snek",True,CYAN)
        TitleScreenWords = BIGFONT.render("You are player " + str(Player + 1),True,CYAN)

    TitleScreenRect = TitleScreenWords.get_rect()
    TitleScreenRect.center = ((xSize/2), (ySize/2))

    ControlsRect = ControlsWords.get_rect()
    ControlsRect.center = ((xSize/2),(ySize - (ySize/3)))

    Window.blit(TitleScreenWords,TitleScreenRect)
    Window.blit(ControlsWords,ControlsRect) 

    #COMING SOON: COUNTDOWN TILL START