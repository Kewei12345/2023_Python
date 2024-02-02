from typing import Any


class Character:

    def __init__(self, CNameP, DOBP, IntelP, SpeedP):
        
        self.CName = CNameP #STRING
        self.DOB = DOBP #STRING
        self.Intel = IntelP #FLOAT
        self.Speed = SpeedP #INTEGER

    
    def GetIntelligence(self):
        return self.Intel
    

    def GetName(self):
        return self.CName
        

    def SetIntelligence(self, IntelPP):
        self.Intel = IntelPP


    def Learn(self):
        self.Intel *= 1.1

        
    def ReturnAge(self):
        Year = int(self.DOB.split("/")[2])
        Age = 2023 - Year
        return Age
        

class MagicCharacter(Character):

    def __init__(self, ElementP, CNameP, DOBP, IntelP, SpeedP):
        super().__init__(CNameP, DOBP, IntelP, SpeedP)
        self.Element = ElementP #STRING

    
    def Learn(self):
        element = self.Element
        match element:
            case "fire":
                self.Intel *= 1.2
            case "water":
                self.Intel *= 1.2
            case "earth":
                self.Intel *= 1.3
            case _ :
                self.Intel *= 1.1

            
                




FirstCharacter = Character("Royal", "01/01/2019", 70.0, 30)
FirstCharacter.Learn()
print(f"Name: {FirstCharacter.GetName()}")
print(f"Age: {FirstCharacter.ReturnAge()}")
print(f"Intelligence: {FirstCharacter.GetIntelligence()}")


FirstMagic = MagicCharacter("fire", "Light", "03/03/2018", 75.0, 22)
FirstMagic.Learn()
print(f"Name: {FirstMagic.GetName()}")
print(f"Age: {FirstMagic.ReturnAge()}")
print(f"Intelligence: {FirstMagic.GetIntelligence()}")