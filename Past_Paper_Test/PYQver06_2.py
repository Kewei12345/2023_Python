class HiddenBox:

    """
    __BoxName : STRING
    __Creator : STRING
    __DateHidden : STRING
    __GameLocation : STRING
    __LastFinds[10][2] : STRING
    __Active : STRING
    """

    def __init__(self, BoxName, Creator, DataHidden, GameLocation):

        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DataHidden = DataHidden
        self.__GameLocation = GameLocation
        self.__Active = False
        self.__LastFinds = [[""]*2]*10


    def GetBoxName(self):

        return (self.__BoxName)

    
    def GetGameLocation(self):

        return (self.__GameLocation)
    

def NewBox(TheBoxes, HeadPointer):

    Name = input("Name: ")
    Creator = input("Creator: ")
    DateHidden = input("Date Hiddden: ")
    GameLocation = input("Game Location: ")

    TheBoxes[HeadPointer] = HiddenBox(Name, Creator, DateHidden, GameLocation)
    HeadPointer += 1
    return HeadPointer


class PuzzleBox(HiddenBox):

    # __PuzzleText : STRING 
    # __Solution : STRING

    def __init__(self, BoxName, Creator, DataHidden, GameLocation, PuzzleText, Solution):

        super().__init__(self, BoxName, Creator, DataHidden, GameLocation)

        self.__PuzzleText = PuzzleText
        self.__Solution = Solution

#main
TheBoxes = [HiddenBox("", "", "", "") for _ in range(10000)]
HeadPointer = 0
HeadPointer = NewBox(TheBoxes, HeadPointer)

    

