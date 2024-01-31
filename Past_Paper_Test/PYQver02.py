class Character: 
    
    def __init__(self, PName, PXPos, PYPos):
        self.Name = PName #STRING
        self.XPos = PXPos #INTEGER
        self.YPos = PYPos #INTEGER

    def GetXPosition(self):
        return self.XPos
    
    def GetYPosition(self):
        return self.YPos
    
    def SetXPosition(self, NewX):
        if self.GetXPosition() + NewX > 10000:
            self.XPos = 10000
        elif self.GetXPosition() + NewX < 0:
            self.XPos = 0
        else:
            self.XPos += NewX

    def SetYPosition(self, NewY):
        if self.GetYPosition() + NewY > 10000:
            self.YPos = 10000
        elif self.GetYPosition() + NewY < 0:
            self.YPos = 0
        else:
            self.YPos += NewY

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(10)
        elif Direction == "down":
            self.SetYPosition(-10)
        elif Direction == "left":
            self.SetXPosition(-10)
        elif Direction == "right":
            self.SetXPosition(10)

class BikeCharacter(Character):
    
    def __init__(self, PName, PXPos, PYPos):
        super().__init__(PName, PXPos, PYPos)

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(20)
        elif Direction == "down":
            self.SetYPosition(-20)
        elif Direction == "left":
            self.SetXPosition(-20)
        elif Direction == "right":
            self.SetXPosition(20)

Jack = Character("Jack", 50, 50)

Karla = BikeCharacter("Karla", 100, 50)

UserChara = input("jack or karla: ")
UserDir = input("Direction: ")

if UserChara.lower() == "jack":
    Jack.Move(UserDir)
    print(f"{UserChara.capitalize()}'s new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
elif UserChara.lower() == "karla":
    Karla.Move(UserDir)
    print(f"{UserChara.capitalize()}'s new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")


