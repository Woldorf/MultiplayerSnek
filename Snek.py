from Game import GameSystem

class Snek:
    def __init__(self,Color,InnerColor,Cords,Direction):
        self.Color = Color
        self.InnerColor = InnerColor
        self.Cords = Cords
        self.Direction = Direction

    def MoveSnek(self,xSize,ySize,CellSize):
        HEAD = 0
        if self.Direction == "L":
            NewHead = {'x': self.Cords[HEAD]['x'] - 1, 'y': self.Cords[HEAD]['y']}
        elif self.Direction == "R":
            NewHead = {'x': self.Cords[HEAD]['x'] + 1, 'y': self.Cords[HEAD]['y']}
        elif self.Direction == "U":
            NewHead = {'x': self.Cords[HEAD]['x'], 'y': self.Cords[HEAD]['y'] - 1}
        elif self.Direction == "D":
            NewHead = {'x': self.Cords[HEAD]['x'], 'y': self.Cords[HEAD]['y'] + 1}

        self.Cords.insert(HEAD,NewHead)

        AppleCords = GameSystem.GetApple()

        if self.Cords[HEAD]["x"] == AppleCords["x"] and self.Cords[HEAD]["y"] == AppleCords["y"]:                
            if AppleCords["Type"] == "Speed":
                del self.Cords[-1]
                GameSystem.MakeApples(xSize,ySize)
                GameSystem.IncreasesTPS()
            elif AppleCords["Type"] == "Board":
                del self.Cords[-1]
                GameSystem.MakeApples(xSize,ySize)
                GameSystem.IncreaseBoard(CellSize)
            elif AppleCords["Type"] == "Normal":
                GameSystem.MakeApples(xSize,ySize)

            