import random

class GameSystem:
    def __init__(self, id,CellsWide,CellsTall):
        self.id = id
        self.Player1Ready = False
        self.Player2Ready = False
        self.GameActive = False
        self.TicksPerSec = 10
        self.CellsWide = CellsWide
        self.CellsTall = CellsTall
        self.P1Ready = False
        self.P2Ready = False
        self.AppleLocation = self.FirstApple()
        self.AppleColor = (255, 0, 0)

    def FirstApple(self):
        x = random.randint(0, self.CellsWide - 1)
        y = random.randint(0, self.CellsTall - 1)
        Type = "Normal"

        return {"x":x,"y":y,"Type":Type}

    def MakeApples(self):
        x = random.randint(0, self.CellsWide - 1)
        y = random.randint(0, self.CellsTall - 1)
        Chance = random.randint(0,201)

        if (Chance % 200) == 0:
            Type = "Master"
        else:
            TypeList=["Normal","Speed","Board"]
            Type = random.choice(TypeList)

        if Type == "Normal":
            self.AppleColor = (255, 0, 0)
        elif Type == "Speed":
            self.AppleColor = (255, 255, 0)
        elif Type == "Board":
            self.AppleColor = (255, 255, 0)
        elif Type == "Master":
            self.AppleColor = (255, 0, 255)

        self.AppleLocation = {'x':x,'y':y,'Type':Type}

    def GetApple(self):
        return self.AppleLocation

    def IncreasesTPS(self):
        self.TicksPerSec += 1

    def GetTPS(self):
        return self.TicksPerSec

    def IncreaseBoard(self,CellSize):
        self.CellsTall += CellSize
        self.CellsWide += CellSize

    def GetBoard(self,CellSize):
        return (self.CellsWide * CellSize), (self.CellsTall * CellSize)