NullP = -1 #CONSTANT

class ListNode:
    def __init__(self, Data=None, Pointer=None):
        self.Data = Data
        self.Pointer = Pointer

List = [ListNode() for i in range(7)]

def InitialiseList():
    global StartP
    global FreeP
    global List

    StartP = NullP
    FreeP = 0
    for i in range(0, 6):
        List[i].Pointer = i + 1
    List[6].Pointer = NullP

InitialiseList()



def InsertNode(NItem):
    global StartP, FreeP, List, New
    if FreeP != NullP:             #Check if array has space
        NewNP = FreeP                
        List[NewNP].Data = NItem     
        FreeP = List[FreeP].Pointer
        """The current node's pointer store next node's pointer"""

        ThisNP = StartP
        PreviousNP = NullP
        while ThisNP != NullP and List[ThisNP].Data < NItem:
            PreviousNP = ThisNP
            ThisNP = List[ThisNP].Pointer
        if PreviousNP == StartP:
            List[NewNP].Pointer = StartP
            StartP = NewNP
        else:
            List[NewNP].Pointer = List[PreviousNP].Pointer
            List[PreviousNP.Pointer] = NewNP

InsertNode("hahaha")
InsertNode("asdhsk")

for j in range(7):
    print(List[j].Data, List[j].Pointer)
    
