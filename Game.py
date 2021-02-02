import random

class GameSystem:
    def __init__(self, id,CellsWide,CellsTall):
        self.id = id
        self.TicksPerSec = 10
        self.CellsWide = CellsWide
        self.CellsTall = CellsTall
        self.CellSize = 20
        self.AppleLocation = self.FirstApple()

    def FirstApple(self):
        x = random.randint(0, self.CellsWide - 1)
        y = random.randint(0, self.CellsTall - 1)
        Type = "Normal"

        return {"x":x,"y":y,"Type":Type}

    def MakeApples(self):
        x = random.randint(0, self.CellsWide - 1)
        y = random.randint(0, self.CellsTall - 1)

        TypeList=["Normal","Speed","Board"]
        Type = random.choice(TypeList)

        self.AppleLocation = {"x":x,"y":y,"Type":Type}

    def GetApple(self):
        return self.AppleLocation

    def IncreasesTPS(self):
        self.TicksPerSec += 1

    def GetTPS(self):
        return self.TicksPerSec

    def IncreaseBoard(self):
        self.CellsTall += self.CellSize
        self.CellsWide += self.CellSize

    def GetBoard(self):
        return (self.CellsWide * self.CellSize), (self.CellsTall * self.CellSize)

    def Logic(self,Snek1,Snek2):
        HEAD = 0
        if Snek1.Cords[HEAD]["x"] == -1 or Snek1.Cords[HEAD]["x"] == self.CellsWide or Snek1.Cords[HEAD]["y"] == -1 or Snek1.Cords[HEAD]["y"] == self.CellsTall\
        or Snek2.Cords[HEAD]["x"] == -1 or Snek2.Cords[HEAD]["x"] == self.CellsWide or Snek2.Cords[HEAD]["y"] == -1 or Snek2.Cords[HEAD]["y"] == self.CellsTall:
            Snek1.Ready = False
            Snek2.Ready = False

        for Segment in Snek1.Cords[1:]:
            if (Segment["x"] == Snek1.Cords[HEAD]["x"] and Segment["y"] == Snek1.Cords[HEAD]["y"])\
            or (Segment["x"] == Snek2.Cords[HEAD]["x"] and Segment["y"] == Snek2.Cords[HEAD]["y"]):
                Snek1.Ready = False
                Snek2.Ready = False

        for Segment in Snek2.Cords[1:]:
            if (Segment["x"] == Snek2.Cords[HEAD]["x"] and Segment["y"] == Snek2.Cords[HEAD]["y"])\
            or (Segment["x"] == Snek1.Cords[HEAD]["x"] and Segment["y"] == Snek1.Cords[HEAD]["y"]):
                Snek1.Ready = False
                Snek2.Ready = False

        #Check if Snek 1 hit an apple
        if Snek1.Cords[HEAD]["x"] == self.AppleLocation["x"] and Snek1.Cords[HEAD]["y"] == self.AppleLocation["y"]:
            if self.AppleLocation["Type"] == "Normal":
                self.MakeApples()
            elif self.AppleLocation["Type"] == "Speed":
                self.MakeApples()
                self.IncreasesTPS()
                del Snek1.Cords[-1]
            elif self.AppleLocation["Type"] == "Board":
                self.MakeApples()
                self.IncreaseBoard()
                del Snek1.Cords[-1]
            else:
                del Snek1.Cords[-1]
        #Check if snek 2 hit an apple
        if Snek2.Cords[HEAD]["x"] == self.AppleLocation["x"] and Snek2.Cords[HEAD]["y"] == self.AppleLocation["y"]:
            if self.AppleLocation["Type"] == "Normal":
                self.MakeApples()
            elif self.AppleLocation["Type"] == "Speed":
                self.MakeApples()
                self.IncreasesTPS()
                del Snek2.Cords[-1]
            elif self.AppleLocation["Type"] == "Board":
                self.MakeApples()
                self.IncreaseBoard()
                del Snek2.Cords[-1]
            else:
                del Snek2.Cords[-1]
        
        return Snek1,Snek2