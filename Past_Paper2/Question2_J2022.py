class Balloon:

    # DECLARE Health : INTEGER
    # DECLARE Colour : STRING
    # DECLARE DefenceItem : STRING

    def __init__(self, DefenceItem, Colour):
        self.__Health = 100
        self.__Colour = Colour
        self.__DefenceItem = DefenceItem

    
    def GetDefenceItem(self):
        return self.__DefenceItem
    

    def ChangeHealth(self, Change):
        self.__Health += Change


    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False
        

UserDefenceItem = input("Enter Defence Item: ")
UserColour = input("Enter Colour: ")
Balloon1 = Balloon(UserDefenceItem, UserColour)


def Defend(Balloon):
    Strength = int(input("Enter Strength of Opponent: "))
    Balloon.ChangeHealth(-Strength)
    print(f"Your Defence Item: {Balloon.GetDefenceItem()}")
    if Balloon.CheckHealth():
        print("You Have No Health Remaining")
    else:
        print("You Have Health Remaining")
    return Balloon


Balloon1 = Defend(Balloon1)