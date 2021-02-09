import pickle,socket,random
from _thread import *
#Home Brewed libraries:
import Game
from Snek import Snek
from Game import GameSystem

server = "192.168.49.248"   
port = 5555
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
    Connection.sendall(pickle.dumps([Players,game]))

    while True:
        try:
            if gameID in games:                
                SnekDirection,PlayerReady,Player = pickle.loads(Connection.recv(4096))
                Players[Player].Direction = SnekDirection
                Players[Player].Ready = PlayerReady

                if Players[0].Ready and Players[1].Ready:
                    Players[0].MoveSnek()
                    Players[1].MoveSnek()
                    Players[0],Players[1] = game.Logic(Players[0],Players[1])
                    
                Connection.sendall(pickle.dumps([Players,game]))

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
    gameID -= 1
    Connection.close()

while True:
    Snek1Cords, Snek1Direction, Snek2Cords, Snek2Direction = Game.GameReset()

    Players = [(Snek(GREEN,DARKGREEN,Snek1Cords,Snek1Direction)),(Snek(BLUE,NAVYBLUE,Snek2Cords,Snek2Direction))]

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