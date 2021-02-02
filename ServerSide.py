import pickle,socket,random
from _thread import *
#Home Brewed libraries:
from Snek import Snek
from Game import GameSystem

server = "192.168.49.248"   
port = 12345

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#             R    G    B
NAVYBLUE  = ( 60,  60, 100)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
CYAN      = (  0, 255, 255)
DARKGREEN = (  0, 155,   0)

try:
    Socket.bind((server, port))
except:
    print("ERROR BINDING")
    pass

Socket.listen(2)
print("Server Started")

connected = set()
games = {}
IDCount = 0

GameHeight = 500
GameWidth = 500

CELLSIZE=20
CellWidth = int(GameWidth / CELLSIZE)
CellHeight = int(GameHeight / CELLSIZE)

def threadedClient(Connection,Player,IDCount,gameID):

    game = games[gameID]

    Connection.sendall(pickle.dumps(Player))
    if Player == 0:
        Connection.sendall(pickle.dumps([Players[0],Players[1],game]))
    else:
        Connection.sendall(pickle.dumps([Players[1],Players[0],game]))

    SnekDirection = Players[Player].Direction

    while True:
        try:
            if gameID in games:
                if not SnekDirection:
                    break
                
                SnekDirection,PlayerReady,Player = pickle.loads(Connection.recv(4096))
                
                if Players[0].Ready and Players[1].Ready:
                    Players[Player].Direction = SnekDirection
                    Players[Player].MoveSnek()
                    Players[0],Players[1] = game.Logic(Players[0],Players[1])
                else:
                    Players[Player].Ready = PlayerReady

                if Player == 0:
                    Connection.sendall(pickle.dumps([Players[0],Players[1],game]))
                else:
                    Connection.sendall(pickle.dumps([Players[1],Players[0],game]))

            else:
                break
        except:
            break

    print("Lost connection to a client")
    try:
        del games[gameID]
        print("Closing Game", gameID)
    except:
        pass
    IDCount -= 1
    Connection.close()

def SnekStartingCords(CELLSIZE):
    DirectionList =["Left","Right","Up","Down"]
    FacingDirection = random.choice(DirectionList)

    StartSquareX = random.randint(3,CELLSIZE-3)
    StartSquareY = random.randint(3,CELLSIZE-3)

    if FacingDirection == "Left":
        DifferenceX = 1
        DifferenceY = 0
    elif FacingDirection == "Right":
        DifferenceX = -1
        DifferenceY = 0
    elif FacingDirection == "Down":
        DifferenceX = 0
        DifferenceY = -1
    elif FacingDirection == "Up":
        DifferenceX = 0
        DifferenceY = 1 

    SnekCordinates =  [
    {"x":StartSquareX, "y":StartSquareY},
    {"x":(StartSquareX + DifferenceX),       "y":(StartSquareY + DifferenceY)},
    {"x":(StartSquareX + 2*DifferenceX), "y":(StartSquareY + 2*DifferenceY)}]

    return SnekCordinates,FacingDirection

TempCordsList,TempDirection = SnekStartingCords(CELLSIZE)
TempCordsList2,TempDirection2 = SnekStartingCords(CELLSIZE)

Players = [(Snek(GREEN,DARKGREEN,TempCordsList,TempDirection)),(Snek(BLUE,NAVYBLUE,TempCordsList2,TempDirection2))]

while True:
    Connection, Address = Socket.accept()

    IDCount += 1
    Player = 0
    gameID = (IDCount - 1)//2

    if IDCount % 2 == 1:
        games[gameID] = GameSystem(gameID,CellWidth,CellHeight)
        print("Creating a new game")
    else:
        Player = 1
    
    start_new_thread(threadedClient, (Connection, Player, IDCount, gameID))
