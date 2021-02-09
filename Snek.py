class Snek:
    def __init__(self,Color,InnerColor,Cords,Direction):
        self.Color = Color
        self.InnerColor = InnerColor
        self.Cords = Cords
        self.Direction = Direction
        self.Ready = False

    def MoveSnek(self):
        HEAD = 0
        if self.Direction == "Left":
            NewHead = {'x': self.Cords[HEAD]['x'] - 1, 'y': self.Cords[HEAD]['y']}
        elif self.Direction == "Right":
            NewHead = {'x': self.Cords[HEAD]['x'] + 1, 'y': self.Cords[HEAD]['y']}
        elif self.Direction == "Up":
            NewHead = {'x': self.Cords[HEAD]['x'], 'y': self.Cords[HEAD]['y'] - 1}
        elif self.Direction == "Down":
            NewHead = {'x': self.Cords[HEAD]['x'], 'y': self.Cords[HEAD]['y'] + 1}
        self.Cords.insert(HEAD,NewHead)